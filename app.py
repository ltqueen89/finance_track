import flet as ft
from views.auth_views import LoginView
from database import DatabaseManager


def main(page:ft.Page):
    page.title = 'Финансовый Трекер'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 800

    db = DatabaseManager(
        host = 'localhost',
        user = 'root',
        password = '2354',
        database = 'flet_projects'  
    )
    
    def route_change(route):
        page.views.clear()
        user_id = page.session.get('user_id')

        if page.route == '/login':
            page.views.append(LoginView(page, db))
        #elif page.route == '/register':
        #   page.views.append(RegisterView(page,db))
        else:   
            if not user_id:
                page.go('/login')
                
        page.update()
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)