# coding=utf-8
from torndb import Row


level = 0


def render_child(right_list):
    """
    绘制子菜单方法，主要用来递归显示子菜单
    :param right_list: 权限集合
    :return:
    """
    html = ''
    for right in right_list:
        right = Row(right)
        global level
        level = level+1
        is_url = False if right.right_url == '#' else True
        href_url = 'javascript:;' if not is_url else right.right_url
        has_sub = 'has-sub' if len(right.child) > 0 else ''
        url_class = ' data-pjax target="_blank"' if is_url else ''
        has_child = len(right.child) > 0
        menu_icon = f'<i class="site-menu-icon {right.icon}" aria-hidden="true"></i>'
        menu_arrow = '<span class="site-menu-arrow"></span>'

        html += f'<li class="site-menu-item {has_sub}">' \
                f'<a href="{href_url}" {url_class}>{menu_icon if level==1 else ""}' \
                f'<span class="site-menu-title">{right.right_name}</span>{menu_arrow if has_child else ""}</a>'
        if has_child:
            html += f'<ul class="site-menu-sub">{render_child(right.child)}</ul>'
        html += '</li>'
        level -= 1
    return html


def menu_tree(right_list, pid):
    """
    为绘制子菜单提供数据
    :param right_list:
    :param pid:
    :return:
    """
    menu_list = []
    if right_list:
        for right in right_list:
            menu_id = right.id
            menu_pid = right.pid
            if menu_pid == pid:
                node = menu_tree(right_list, menu_id)
                right["child"] = node
                menu_list.append(right)
    return menu_list


def right_tree(right_list, pid):
    """
    权限树形结构数据
    :param right_list:
    :param pid:
    :return:
    """
    tree = []
    if right_list:
        for right in right_list:
            node = {}
            if pid == right.pid:
                node['layer'] = right.id
                node['icon'] = right.icon
                node['tenantId'] = '8'
                node['id'] = right.id
                node['text'] = right.right_name
                c_node = right_tree(right_list, right.id)
                node['children'] = c_node
                if right.state == 'true':
                    state = {'selected': True}
                    node['state'] = state
                tree.append(node)
    return tree
