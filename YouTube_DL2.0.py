from yt_dlp import YoutubeDL
import flet as ft
import tkinter as tk
from tkinter import filedialog

def main(page:ft.page):
    page.window_width = 500
    page.window_height = 300
    page.window_maximizable = False
    page.title = "YT_Downloader"
    welcome = ft.Text(value="Welcome to YT_Downloader!", size=25, color="blue")
    filetype = ft.RadioGroup(
        value="FileType",
        content=ft.Row([
            ft.Radio(value="MP3", label="MP3"),
            ft.Radio(value="MP4", label="MP4"),
        ]),
    )
    url_field = ft.TextField(label="Please enter the URL")

    def DL(event):
        url = url_field.value
        if filetype.value == "MP3":
            ydl_audio_opts = {
                'format': 'bestaudio/best',
                'outtmpl': filedialog.asksaveasfilename(defaultextension=".mp3")
                }
            with YoutubeDL(ydl_audio_opts) as ydl:
                download = ydl.download([url])
        if filetype.value == "MP4":
            ydl_video_opts = {
                'format': 'best',
                'outtmpl': filedialog.asksaveasfilename(defaultextension=".mp4")
                }
            with YoutubeDL(ydl_video_opts) as ydl:
                download = ydl.download([url])

    button = ft.FilledButton("Download", on_click=DL)
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        welcome, filetype, url_field, button
                    ], spacing=20,
                ), padding=20
            ), margin=20
        )
    )


ft.app(target=main)