/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50640
 Source Host           : localhost:3306
 Source Schema         : vmms

 Target Server Type    : MySQL
 Target Server Version : 50640
 File Encoding         : 65001

 Date: 05/03/2019 17:26:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sys_access_token
-- ----------------------------
DROP TABLE IF EXISTS `sys_access_token`;
CREATE TABLE `sys_access_token`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `access_token` varchar(520) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `expirse_in` int(5) NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_btn
-- ----------------------------
DROP TABLE IF EXISTS `sys_btn`;
CREATE TABLE `sys_btn`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `btn_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `btn_desc` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_dic
-- ----------------------------
DROP TABLE IF EXISTS `sys_dic`;
CREATE TABLE `sys_dic`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dc_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dc_k` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dc_v` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `dc_desc` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `seq` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_dic
-- ----------------------------
INSERT INTO `sys_dic` VALUES ('1', 'tools_type', '1', '浏览器相关', '各种浏览器', '0', '0');
INSERT INTO `sys_dic` VALUES ('2', 'tools_type', '2', '系统安全相关', '安全杀毒软件', '5', '0');
INSERT INTO `sys_dic` VALUES ('3', 'tools_type', '3', '编程软件相关', '编程类型的工具', '10', '0');
INSERT INTO `sys_dic` VALUES ('4', 'tools_type', '4', '数据恢复相关', '数据恢复类工具', '15', '0');
INSERT INTO `sys_dic` VALUES ('5', 'tools_type', '5', '教育相关', '教育类型的工具', '20', '0');
INSERT INTO `sys_dic` VALUES ('91', 'plat_label', '1', 'windows', 'windows平台', '0', '0');
INSERT INTO `sys_dic` VALUES ('92', 'plat_label', '2', 'mac', '苹果电脑', '5', '0');
INSERT INTO `sys_dic` VALUES ('93', 'plat_label', '3', 'android', '安卓', '10', '0');
INSERT INTO `sys_dic` VALUES ('94', 'plat_label', '4', 'ios', 'iphone', '15', '0');

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `method_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remote_ip` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `req_uri` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_log
-- ----------------------------
INSERT INTO `sys_log` VALUES ('13655f16b51744de92af96f4a35e0511', 'com.zhx.gmms.modules.sys.LoginController', 'index', '192.168.5.229', '/index', '', '2018-09-06 16:02:22', NULL);
INSERT INTO `sys_log` VALUES ('1bef4d63813e40b4baab89b925123b3f', 'com.zhx.gmms.modules.sys.LoginController', 'captcha', '192.168.5.229', '/captcha', '', '2018-09-06 16:02:22', NULL);
INSERT INTO `sys_log` VALUES ('1dd4633ec764494faf73addefdb7f168', 'com.zhx.gmms.modules.sys.LoginController', 'captcha', '192.168.5.229', '/captcha', '', '2018-09-06 16:06:34', NULL);
INSERT INTO `sys_log` VALUES ('5d593ed29cba4ff188354df1859274a1', 'com.zhx.gmms.modules.sys.LoginController', 'loginIn', '192.168.5.229', '/loginIn', '', '2018-09-06 16:03:02', NULL);
INSERT INTO `sys_log` VALUES ('701a1b139caa4b3aaeafabfe1c7b5866', 'com.zhx.gmms.modules.sys.role.controller.SysRoleController', 'roleUserCounts', '192.168.5.229', '/role/usercounts', '1', '2018-09-06 16:03:12', NULL);
INSERT INTO `sys_log` VALUES ('c15d074e35f74df4b56c448fd21bbeaf', 'com.zhx.gmms.modules.sys.user.controller.SysUserController', 'userList', '192.168.5.229', '/user/pagelist', '1', '2018-09-06 16:03:12', NULL);
INSERT INTO `sys_log` VALUES ('e6598786f92348d9b3905eac5e8251fd', 'com.zhx.gmms.modules.sys.user.controller.SysUserController', 'findList', '192.168.5.229', '/user/list', '1', '2018-09-06 16:03:12', NULL);
INSERT INTO `sys_log` VALUES ('e8bc06b6b17a4a5f836d38b70e2eee19', 'com.zhx.gmms.modules.sys.LoginController', 'index', '192.168.5.229', '/index', '', '2018-09-06 16:06:33', NULL);
INSERT INTO `sys_log` VALUES ('f597c5e0982448c8b47d3cca0fffa704', 'com.zhx.gmms.modules.sys.LoginController', 'home', '192.168.5.229', '/home', '1', '2018-09-06 16:03:02', NULL);

-- ----------------------------
-- Table structure for sys_right
-- ----------------------------
DROP TABLE IF EXISTS `sys_right`;
CREATE TABLE `sys_right`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `right_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `right_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `right_desc` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_leaf` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1',
  `icon` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '0',
  `seq` int(5) NULL DEFAULT 0,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_right
-- ----------------------------
INSERT INTO `sys_right` VALUES ('0', '-1', '系统菜单', '#', '系统菜单', '0', 'fa-laptop', '0', 0, '1', '2017-11-08 09:40:56', NULL, NULL);
INSERT INTO `sys_right` VALUES ('001001', '1', '后台管理', '#', '后台管理', '1', 'fa-laptop', '0', 0, '1', '2018-08-30 17:10:26', NULL, NULL);
INSERT INTO `sys_right` VALUES ('001001001', '001001', '菜单管理', '/right/list', '菜单管理', '1', 'fa-laptop', '0', 0, '1', '2018-08-30 14:18:06', NULL, NULL);
INSERT INTO `sys_right` VALUES ('001001002', '001001', '用户管理', '/user/list', '用户管理', '1', 'fa-laptop', '0', 5, '1', '2017-11-03 12:48:27', '1', '2017-11-07 15:05:14');
INSERT INTO `sys_right` VALUES ('001001003', '001001', '日志管理', '/log/list', '日志管理', '1', 'fa-laptop', '0', 10, '1', '2017-11-03 18:32:09', NULL, NULL);
INSERT INTO `sys_right` VALUES ('001002', '1', '显示管理', '#', '显示管理', '1', 'fa-laptop', '0', 5, '1', '2018-08-30 17:12:10', NULL, NULL);
INSERT INTO `sys_right` VALUES ('001002001', '001002', '主题设置', 'system/settings', '主题设置', '1', 'fa-laptop', '0', 0, '1', '2019-03-01 09:41:43', NULL, '2019-03-01 09:41:43');
INSERT INTO `sys_right` VALUES ('002001', '2', '业务菜单111', '#', '业务菜单', '1', 'fa-laptop', '0', 0, '1', '2019-02-28 16:08:34', NULL, '2019-02-28 16:08:34');
INSERT INTO `sys_right` VALUES ('018aaeae40ce6a5504b8c3152abd3e14', 'f649be1ec4074eeaa802d75c264224e8', '测试子菜单1', '#', '', '1', 'fa-bell-o', '1', 5, '1', '2019-02-28 15:31:25', '', '2019-02-28 15:31:25');
INSERT INTO `sys_right` VALUES ('1', '0', '系统设置', '#', '系统设置', '0', 'wb-settings', '0', 0, '1', '2018-08-31 16:38:50', NULL, '2018-08-31 16:38:50');
INSERT INTO `sys_right` VALUES ('2', '0', '业务页面', '#', '业务页面', '1', 'wb-extension', '0', 10, '1', '2019-02-25 17:03:57', NULL, '2019-02-25 17:03:57');
INSERT INTO `sys_right` VALUES ('3d10dab5866045a696d6e522b34b27f8', '0', '测试菜单', '#', '', '1', 'fa-bars', '1', 10, '1', '2019-02-22 16:38:53', '', '2019-02-22 16:38:53');
INSERT INTO `sys_right` VALUES ('838f60e2f15796bde7f0376362ee1101', '002001', '自定义菜单', '#', '', '1', '', '0', 5, '1', '2019-02-28 16:18:51', '', '2019-02-28 16:18:51');
INSERT INTO `sys_right` VALUES ('a5694c4c6c3c57533bac9e4a13ed2d4c', '2', '自定义菜单', '#', '', '1', 'fa-bars', '0', 5, '1', '2019-02-28 16:18:10', '', '2019-02-28 16:18:10');
INSERT INTO `sys_right` VALUES ('a9ad82c953974292ae5f71b30774c619', 'f649be1ec4074eeaa802d75c264224e8', '自定义菜单一', '#', '', '1', 'fa-file-o', '1', 10, '1', '2019-02-28 16:40:41', '', '2019-02-28 16:40:41');
INSERT INTO `sys_right` VALUES ('c9895a13df129a31d4f5c9f434557de8', 'a5694c4c6c3c57533bac9e4a13ed2d4c', '自定义菜单', '#', '', '1', '', '0', 5, '1', '2019-02-28 16:22:54', '', '2019-02-28 16:22:54');
INSERT INTO `sys_right` VALUES ('f649be1ec4074eeaa802d75c264224e8', '0', '测试菜单', '#', '', '1', 'wb-chat', '0', 5, '1', '2019-02-26 09:16:28', '', '2019-02-26 09:16:28');

-- ----------------------------
-- Table structure for sys_right_btn
-- ----------------------------
DROP TABLE IF EXISTS `sys_right_btn`;
CREATE TABLE `sys_right_btn`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `right_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `btn_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `role_desc` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '0',
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES ('03da14eba8274604839dbe5959467135', '测试角色1', '测试角色1', '1', '', '2019-03-01 09:44:13', '', '2019-03-01 09:44:13');
INSERT INTO `sys_role` VALUES ('1', '超级管理员', '所有权限', '0', '1', '2017-11-03 11:48:52', NULL, NULL);
INSERT INTO `sys_role` VALUES ('2', '开发', NULL, '0', NULL, NULL, NULL, NULL);
INSERT INTO `sys_role` VALUES ('3', '测试', NULL, '0', NULL, NULL, NULL, NULL);
INSERT INTO `sys_role` VALUES ('3a5d4bfd898743ca9aa22df28466920f', '测试角色', '测试角色', '1', '', '2019-03-01 09:46:54', '', '2019-03-01 09:46:54');
INSERT INTO `sys_role` VALUES ('d3b45aecb5eb433ea220350124bcab8c', '测试角色2', '测试角色2', '1', '', '2019-03-01 09:55:01', '', '2019-03-01 09:55:01');

-- ----------------------------
-- Table structure for sys_role_right
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_right`;
CREATE TABLE `sys_role_right`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `right_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_role_right
-- ----------------------------
INSERT INTO `sys_role_right` VALUES ('001001', '1', '001001', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('001001001', '1', '001001001', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('001001002', '1', '001001002', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('001001003', '1', '001001003', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('001002', '1', '001002', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('001002001', '1', '001002001', '1', NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('030bea93e07849c390a4996de1c83607', '1', '3d10dab5866045a696d6e522b34b27f8', '1', '', '2019-02-22 16:38:53', '', '2019-02-22 16:38:53');
INSERT INTO `sys_role_right` VALUES ('03443ab7aced4580be3f67dddbc04751', '3', '3d10dab5866045a696d6e522b34b27f8', '1', '', '2019-02-22 16:38:53', '', '2019-02-22 16:38:53');
INSERT INTO `sys_role_right` VALUES ('061e6e12b37a4433bc59c16f055e53f6', 'd3b45aecb5eb433ea220350124bcab8c', '838f60e2f15796bde7f0376362ee1101', '1', '', '2019-03-01 09:55:01', '', '2019-03-01 09:55:01');
INSERT INTO `sys_role_right` VALUES ('13924697eeba45018b4c729260adb6a3', '1', 'e014b02f7f8443949df47b4e2a089cf6', '0', '', '2019-02-28 16:28:01', '', '2019-02-28 16:28:01');
INSERT INTO `sys_role_right` VALUES ('2', '1', '2', '1', NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('21a5fe82c22b452c8bc2647b157f3ee4', 'd3b45aecb5eb433ea220350124bcab8c', '002001', '1', '', '2019-03-01 09:55:02', '', '2019-03-01 09:55:02');
INSERT INTO `sys_role_right` VALUES ('2a5a53598d914548bf41403069b9d44b', '1', '2', '0', '', '2019-02-25 17:03:57', '', '2019-02-25 17:03:57');
INSERT INTO `sys_role_right` VALUES ('4ed4a3186dae467083fbd20667d297a0', '3', '001002001', '0', '', '2019-03-01 09:41:43', '', '2019-03-01 09:41:43');
INSERT INTO `sys_role_right` VALUES ('57720439c0174b938a291af7c12dad79', '1', '002001', '1', '', '2019-02-22 17:13:12', '', '2019-02-22 17:13:12');
INSERT INTO `sys_role_right` VALUES ('59219b318e854d5ba8b383e2033c33eb', '2', '3d10dab5866045a696d6e522b34b27f8', '1', '', '2019-02-22 16:38:53', '', '2019-02-22 16:38:53');
INSERT INTO `sys_role_right` VALUES ('595f773fe68348078271cd4d17e92ba1', '2', '002001', '1', '', '2019-02-22 17:13:12', '', '2019-02-22 17:13:12');
INSERT INTO `sys_role_right` VALUES ('5f874d7f4ea544c68ac6cf35e0172bea', '1', '3d10dab5866045a696d6e522b34b27f8', '1', '', '2019-02-22 16:26:52', '', '2019-02-22 16:26:52');
INSERT INTO `sys_role_right` VALUES ('637de0c334d4425490ab5d668b65e361', '3', '002001', '1', '', '2019-02-22 17:13:12', '', '2019-02-22 17:13:12');
INSERT INTO `sys_role_right` VALUES ('64c01ac603314b8cbd7159b09c3b0d0a', '1', '002001', '1', '', '2019-02-22 16:55:32', '', '2019-02-22 16:55:32');
INSERT INTO `sys_role_right` VALUES ('652ad9ef5b5e463ea0aaf487ac4a5d8a', '1', '001002001', '0', '', '2019-03-01 09:41:43', '', '2019-03-01 09:41:43');
INSERT INTO `sys_role_right` VALUES ('7d4ebbfd82da48038c9faef6f719ccd7', '1', '1', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `sys_role_right` VALUES ('8a77279e2a1b45f3b8d49079a06450bd', '2', '001002001', '0', '', '2019-03-01 09:41:43', '', '2019-03-01 09:41:43');
INSERT INTO `sys_role_right` VALUES ('bfe14d51512d487c8d748ea983ad88cb', '03da14eba8274604839dbe5959467135', 'f649be1ec4074eeaa802d75c264224e8', '1', '', '2019-03-01 09:44:14', '', '2019-03-01 09:44:14');
INSERT INTO `sys_role_right` VALUES ('c7f7c404c5e74715ad147c16ebc2d019', '1', '018aaeae40ce6a5504b8c3152abd3e14', '1', '', '2019-02-28 15:27:25', '', '2019-02-28 15:27:25');
INSERT INTO `sys_role_right` VALUES ('cb5a487ef1ef45269938b5653ceb49c9', 'd3b45aecb5eb433ea220350124bcab8c', '2', '1', '', '2019-03-01 09:55:01', '', '2019-03-01 09:55:01');
INSERT INTO `sys_role_right` VALUES ('d15b8cf969e545518f2854552ef06cf6', '3a5d4bfd898743ca9aa22df28466920f', 'f649be1ec4074eeaa802d75c264224e8', '1', '', '2019-03-01 09:46:54', '', '2019-03-01 09:46:54');
INSERT INTO `sys_role_right` VALUES ('ef1b6675bcfe457bb180005be74435c9', 'd3b45aecb5eb433ea220350124bcab8c', 'a5694c4c6c3c57533bac9e4a13ed2d4c', '1', '', '2019-03-01 09:55:02', '', '2019-03-01 09:55:02');
INSERT INTO `sys_role_right` VALUES ('f2a60f1a426a463a8382884ff0a2fba8', 'd3b45aecb5eb433ea220350124bcab8c', 'c9895a13df129a31d4f5c9f434557de8', '1', '', '2019-03-01 09:55:01', '', '2019-03-01 09:55:01');
INSERT INTO `sys_role_right` VALUES ('f8a19079c4c547cf85ae35839de1dc8d', '1', 'f649be1ec4074eeaa802d75c264224e8', '0', '', '2019-02-26 09:16:28', '', '2019-02-26 09:16:28');
INSERT INTO `sys_role_right` VALUES ('fef83e3cc57a40298f84d3814c333a5a', '03da14eba8274604839dbe5959467135', 'f649be1ec4074eeaa802d75c264224e8', '1', '', '2019-03-01 09:42:00', '', '2019-03-01 09:42:00');

-- ----------------------------
-- Table structure for sys_theme
-- ----------------------------
DROP TABLE IF EXISTS `sys_theme`;
CREATE TABLE `sys_theme`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sidebar` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `navbar` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `navbar_inverse` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `theme_color` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_display` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `menu_txt_icon` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tab_flag` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_theme
-- ----------------------------
INSERT INTO `sys_theme` VALUES ('-1', 'site-menubar-dark', 'bg-primary-600', 'navbar-inverse', '', 'site-menubar-unfold', 'site-menubar-keep', 'site-contabs-open', NULL);
INSERT INTO `sys_theme` VALUES ('cc2edb6b180940a0be6c59eaea5463ea', 'site-menubar-light', 'bg-indigo-600', 'navbar-inverse', 'indigo', 'site-menubar-unfold', 'site-menubar-keep', 'site-contabs-open', NULL);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_code` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nick_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mail` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `use_status` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 'NORMAL',
  `last_login_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `login_total` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `theme_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '-1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES ('1', 'xwl5242@163.com', 'xwl', 'f3e35768370a8b2f3b3640a9d2ddc34b7e08cf4da92d', 'XWL', '15313685599', 'xwl5242@163.com', '0', '23', '1', 'NORMAL', '2019-02-28 08:52:24', '513', '0', '1', '2017-11-02 18:02:26', '', '2018-05-28 14:09:25', 'cc2edb6b180940a0be6c59eaea5463ea');
INSERT INTO `sys_user` VALUES ('1111', 'xwl5242@163.com111', 'xwl', 'f3e35768370a8b2f3b3640a9d2ddc34b7e08cf4da92d', 'XWL', '15313685599', 'xwl5242@163.com', '0', '23', '1', 'NORMAL', '2018-09-13 16:29:00', '387', '0', '1', '2017-11-02 18:02:26', '', '2018-05-28 14:09:25', 'cc2edb6b180940a0be6c59eaea5463ea');

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `role_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `creator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `updator` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_user_role
-- ----------------------------
INSERT INTO `sys_user_role` VALUES ('1', '1', '1', NULL, '1', '2017-11-03 11:49:10', NULL, NULL);
INSERT INTO `sys_user_role` VALUES ('2', '1', '2', NULL, '1', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for t_banner
-- ----------------------------
DROP TABLE IF EXISTS `t_banner`;
CREATE TABLE `t_banner`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `seq` int(2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_banner
-- ----------------------------
INSERT INTO `t_banner` VALUES ('1', '/imgs/index/banner_1.jpg', '美食', NULL, '2019-03-04 10:30:00', '0', 0);
INSERT INTO `t_banner` VALUES ('2', '/imgs/index/banner_2.jpg', '美食', NULL, '2019-03-04 10:30:00', '0', 5);
INSERT INTO `t_banner` VALUES ('3', '/imgs/index/banner_3.jpg', '美食', NULL, '2019-03-04 10:30:00', '0', 10);

-- ----------------------------
-- Table structure for t_base_tools
-- ----------------------------
DROP TABLE IF EXISTS `t_base_tools`;
CREATE TABLE `t_base_tools`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `img_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `detail_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stars` int(2) NULL DEFAULT NULL,
  `score` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `seq` int(3) NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_base_tools
-- ----------------------------
INSERT INTO `t_base_tools` VALUES ('1', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'google浏览器', '1', 6, '8.8', '2019-03-04 08:35:00', 0, '0');
INSERT INTO `t_base_tools` VALUES ('10', '3', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'pycharm', NULL, 6, '8.8', '2019-03-04 08:35:00', 5, '0');
INSERT INTO `t_base_tools` VALUES ('11', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', '2345浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 30, '0');
INSERT INTO `t_base_tools` VALUES ('12', '4', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'u盘数据恢复', NULL, 6, '8.8', '2019-03-04 08:35:00', 0, '0');
INSERT INTO `t_base_tools` VALUES ('2', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', '360浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 5, '0');
INSERT INTO `t_base_tools` VALUES ('3', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'firefox浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 10, '0');
INSERT INTO `t_base_tools` VALUES ('4', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'ie浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 15, '0');
INSERT INTO `t_base_tools` VALUES ('5', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', '欧朋浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 20, '0');
INSERT INTO `t_base_tools` VALUES ('6', '1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'UC浏览器', NULL, 6, '8.8', '2019-03-04 08:35:00', 25, '0');
INSERT INTO `t_base_tools` VALUES ('7', '2', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', '金山毒霸', NULL, 6, '8.8', '2019-03-04 08:35:00', 0, '0');
INSERT INTO `t_base_tools` VALUES ('8', '2', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', '360杀毒', NULL, 6, '8.8', '2019-03-04 08:35:00', 5, '0');
INSERT INTO `t_base_tools` VALUES ('9', '3', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg', 'eclipse', NULL, 6, '8.8', '2019-03-04 08:35:00', 0, '0');

-- ----------------------------
-- Table structure for t_detail_tools
-- ----------------------------
DROP TABLE IF EXISTS `t_detail_tools`;
CREATE TABLE `t_detail_tools`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img_urls` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详情中的图片地址，最多支持4张，多个中间用逗号分隔',
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标题',
  `comments` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '详情介绍',
  `plat_label` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '平台标签，多个中间用逗号分隔',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注信息',
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_detail_tools
-- ----------------------------
INSERT INTO `t_detail_tools` VALUES ('1', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.jpg;', 'google浏览器', 'google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器<br>google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器;google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器;google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器;google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器;google浏览器，开发人员最爱，开发利器，世界上最受欢迎的浏览器;', '1,2,3,4', NULL, '2019-03-04 11:45:00', '0');

-- ----------------------------
-- Table structure for t_icon
-- ----------------------------
DROP TABLE IF EXISTS `t_icon`;
CREATE TABLE `t_icon`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `img_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fragment` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '锚点，点击icon跳转到页面哪一部分，和tools_type关联',
  `create_time` varchar(22) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_del` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `seq` int(2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_icon
-- ----------------------------
INSERT INTO `t_icon` VALUES ('1', '/imgs/index/icon_1.jpg', '浏览器', '1', '2019-03-04 10:52:00', '0', 0);
INSERT INTO `t_icon` VALUES ('2', '/imgs/index/icon_2.jpg', '系统安全', '2', '2019-03-04 10:52:00', '0', 0);
INSERT INTO `t_icon` VALUES ('3', '/imgs/index/icon_3.jpg', '编程工具', '3', '2019-03-04 10:52:00', '0', 0);
INSERT INTO `t_icon` VALUES ('4', '/imgs/index/icon_4.jpg', '数据恢复', '4', '2019-03-04 10:52:00', '0', 0);
INSERT INTO `t_icon` VALUES ('5', '/imgs/index/icon_5.jpg', '教育', '5', '2019-03-04 10:52:00', '0', 0);

-- ----------------------------
-- Function structure for getChildList
-- ----------------------------
DROP FUNCTION IF EXISTS `getChildList`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `getChildList`(rootId INT) RETURNS varchar(1000) CHARSET utf8
BEGIN
DECLARE sTemp VARCHAR(1000);
DECLARE sTempChd VARCHAR(1000);

SET sTemp = '$';
SET sTempChd =cast(rootId as CHAR);

WHILE sTempChd is not null DO
SET sTemp = concat(sTemp,',',sTempChd);
SELECT group_concat(id) INTO sTempChd FROM sys_right where FIND_IN_SET(pid,sTempChd)>0;
END WHILE;
RETURN sTemp;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
