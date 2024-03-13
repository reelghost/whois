from ipwhois import IPWhois
import json
import flet as ft


def main(page: ft.Page):
    def get_ip_info(e):
        if not ip_input.value:
            ip_input.error_text = "Please enter an IP or Domain"
            page.update()
        else:
            ip_address = ip_input.value
            try:
                obj = IPWhois(ip_address)
                result = obj.lookup_whois()
                country = result["nets"][0]['country']
                name = result["nets"][0]['name']
                address = result["nets"][0]['address']
                description = result["nets"][0]['description']

                info = {
                    "country": country,
                    "name": name,
                    "address": address,
                    "description": description
                }
            except Exception as e:
                info = {
                    "error": str(e)
                }
            # page.clean()
            page.add(ft.Text(f"Country: {info['country']}"))
        

    page.title = 'Whois App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    t = ft.Text(value="Welcome to whois App",
                color="green", text_align="center", size="60", weight="bold")
    

    look_up_btn = ft.CupertinoFilledButton(content=ft.Text("LOOKUP", text_align="center", weight="bold"), on_click=get_ip_info)
    ip_input = ft.TextField(label="Input the domain", expand=True)

    input_view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    ip_input,
                    look_up_btn,
                ],
            ),
        ],
    )
    page.controls.append(t)
    page.add(input_view)
    page.update()


# if __name__ == "__main__":
#     ip_address = "197.232.243.115"
#     ip_info = get_ip_info(ip_address)
#     print(ip_info)
ft.app(main)

