from tkinter import *
from newsapi import NewsApiClient

news = NewsApiClient(api_key="ENTER API KEY HERE")

footer_text = "Copyright © SmashedFrenzy16 and SmashedFrenzy16 Studios under the Apache 2.0 License"

class App(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for i in (Start, Headlines, Articles):

            frame = i(container, self)

            self.frames[i] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, contn):

        frame = self.frames[contn]

        frame.tkraise()


class Start(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        welcome_label = Label(
            self, fg="red", text="Welcome To ONews!", font=("Arial", 96))

        welcome_label.pack()

        blank_label = Label(self, text="")

        blank_label.pack()

        button_headlines = Button(
            self, text="Headlines ⇒", fg="red", bg="black", font=("Arial", 72), command=lambda: controller.show_frame(Headlines))

        button_headlines.pack()

        blank_label2 = Label(self, text="")

        blank_label2.pack()

        button_articles = Button(
            self, text="All Articles ⇒", fg="red", bg="black", font=("Arial", 72), command=lambda: controller.show_frame(Articles))

        button_articles.pack()

        footer = Label(self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)


class Headlines(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        headlines_label = Label(
            self, fg="red", text="Headlines", font=("Arial", 96))

        headlines_label.pack()

        button_back_h = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_h.place(x=0, y=20, anchor=W)

        blank_label = Label(self, text="")

        blank_label.pack()

        headline_e = Entry(self, width=100, borderwidth=5)

        headline_e.pack()

        headline_e.insert(0, "Enter a query")

        def execution():

            headlines = headline_e.get()

            top_headlines = news.get_top_headlines(q=headlines,
                                                   category='technology',
                                                   language='en',
                                                   country='us')

            scrollbar1 = Scrollbar(self)

            scrollbar1.pack(side=RIGHT, fill=Y)

            list1 = Listbox(self, yscrollcommand=scrollbar1.set)

            for key in top_headlines:

                list1.insert(END, f"{key}: {top_headlines[key]}")

            list1.pack()



        execute_button = Button(self, text="Enter", command=execution)

        execute_button.pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)

class Articles(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        articles_label = Label(
            self, fg="red", text="All Articles", font=("Arial", 96))

        articles_label.pack()

        button_back_a = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_a.place(x=0, y=20, anchor=W)

        blank_label = Label(self, text="")

        blank_label.pack()

        article_e = Entry(self, width=100, borderwidth=5)

        article_e.pack()

        article_e.insert(0, "Enter a query")

        def execution():

            articles = article_e.get()

            all_articles = news.get_everything(q=articles,
                                                  sources='bbc-news,the-verge',
                                                  domains='bbc.co.uk,techcrunch.com',
                                                  from_param='2023-02-28',
                                                  to='2023-03-29',
                                                  language='en',
                                                  sort_by='relevancy',
                                                  page=2)

            scrollbar1 = Scrollbar(self)

            scrollbar1.pack(side=RIGHT, fill=Y)

            list1 = Listbox(self, yscrollcommand=scrollbar1.set)

            for key in all_articles:

                list1.insert(END, f"{key}: {all_articles[key]}")

            list1.pack()

        execute_button = Button(self, text="Enter", command=execution)

        execute_button.pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)


root = App()

root.title("ONews By @SmashedFrenzy16")

root.geometry("1000x1000")

root.mainloop()
