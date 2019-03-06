# coding=utf-8
import gzip
import json
from io import BytesIO
from web.sys.captcha import Captcha
from web.base.base_handler import BaseHandler
from web.util.AESUtil import AESUtil
from web.util.MenuUtil import menu_tree, render_child
from modules.sys.user import User
from modules.sys.theme import Theme
from modules.sys.right import Right
from tornado.web import authenticated


class CaptchaHandler(BaseHandler):
	"""
	生成验证码hanlder
	"""
	def get(self):
		captcha = Captcha(120, 40, ch_len=4)
		code_img, code = captcha.render_code()
		msstream = BytesIO()
		code_img.save(msstream, "png")
		code_img.close()
		self.set_secure_cookie("verify_code", code)
		self.set_header('Content-Type', 'image/jpg')
		self.write(msstream.getvalue())


class HomeHandler(BaseHandler):
	"""
	首页
	"""
	@authenticated
	def get(self):
		self.render_('index.html')


class LoginHandler(BaseHandler):
	"""
	登录相关handler
	"""
	def get(self):
		self.render("login.html", message=None)

	def post(self):
		user_id = self.get_current_user()

		user_code = self.get_argument("userCode")
		password = self.get_argument("password")
		need_captcha = self.get_argument("needCaptcha")

		if need_captcha == str(True):
			valid_code = self.get_argument("validCode")

		valid_pass = True if need_captcha == str(False) else \
			(valid_code.upper() == self.get_secure_cookie("verify_code").decode("utf-8"))

		if valid_pass:
			user = User.get_by_code(user_code)
			if user is None:
				self.render("login.html", message="用户不存在!")
			elif password != AESUtil.decrypt(user.password):
				self.render("login.html", message="用户密码不正确!")
			else:
				# 登录成功,获取当前登录用户的主题信息
				theme = Theme.get_by_user_id(user.id)
				# 登录成功,获取当前登录用户的权限信息
				rights = Right.query_by_user_id(user.id)
				menu = menu_tree(right_list=rights, pid="0")
				# 更新用户相关信息
				if not user_id:
					sql = f"update sys_user set last_login_time=now(),login_total=login_total+1 where id = {user.id}"
					User.update_by_sql(sql)
				# 保存相关信息,并跳转
				self.set_secure_cookie("right", gzip.compress(json.dumps(menu).encode()))
				self.set_secure_cookie("userId", user.id)
				self.set_secure_cookie("themeId", theme.id)
				self.set_secure_cookie("user", gzip.compress(json.dumps(user).encode()))
				self.set_secure_cookie("theme", gzip.compress(json.dumps(theme).encode()))
				self.render("index.html", user=user, theme=theme, theme_json=json.dumps(theme), right=menu, render_child=render_child, T_N=self.T_N)
		else:
			self.render("login.html", message="验证码填写错误!")


class LogoutHandler(BaseHandler):
	"""
	退出登录
	"""
	def get(self):
		self.clear_cookies()
		self.redirect(url='/')
