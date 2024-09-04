import tkinter as tk


root = tk.Tk()
root.geometry('700x750')
root.resizable(False, False)
root.title = 'ვალუტის კურსი'


background_image = tk.PhotoImage(file='currency.img.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)


text_label = tk.Label(root,
                     text='ვალუტის კურსი',
                     font=('italic', 30),
                     fg='#137520',
                     bg='#E2E234')
text_label.pack()


#მარცხენა frame
frame = tk.Frame(width=400, height=500, bg='#E47900')
frame.place(x=20, y=280)


label2 = tk.Label(frame,
                  text='აირჩიეთ სასურველი ვალუტა',
                  bg='#E2FF22',
                  fg='#326939',
                  font=('arial', 13))
label2.pack()


#ტექსტის გამოსატანი(1)
output_label = tk.Label(root,
                        text='',
                        font=('arial', 18),
                        fg='#137520',
                        bg='#E2E234')
output_label.pack(pady=20)


selected_from = tk.StringVar()
selected_to = tk.StringVar()


def button_func1():
   selected_from.set('$')
   output_label.config(text='თქვენ ყიდით დოლარს')


def button_func2():
   selected_from.set('₾')
   output_label.config(text='თქვენ ყიდით ლარს')


def button_func3():
   selected_from.set('€')
   output_label.config(text='თქვენ ყიდით ევროს')


def button_func4():
   selected_from.set('₺')
   output_label.config(text='თქვენ ყიდით ლირას')




button1 = tk.Button(frame,
                    text='$',
                    width=2,
                    height=2,
                    font=('bold', 12),
                    bg='#49DE4E',
                    command=button_func1)
button1.pack(side='left', padx=20, pady=2)


button2 = tk.Button(frame,
                    text='₾',
                    width=2,
                    height=2,
                    font=('bold', 12),
                    bg='#49DE4E',
                    command=button_func2)
button2.pack(side='left', padx=20, pady=2)


button3 = tk.Button(frame,
                    text='€',
                    width=2,
                    height=2,
                    font=('bold',12),
                    bg='#49DE4E',
                    command=button_func3)
button3.pack(side='left', padx=20, pady=2)


button4 = tk.Button(frame,
                    text='₺',
                    width=2,
                    height=2,
                    font=('bold', 12),
                    bg='#49DE4E',
                    command=button_func4)
button4.pack(side='left', padx=20, pady=5)


label_from_where = tk.Label(frame, text = ('საიდან'), font = ('arial', 10), bg = '#E2FF22')
label_from_where.pack(side = 'left', padx = 5, pady = 3)


#მარჯვენა frame
frame2 = tk.Frame(root, width=400, height=200, bg='#E47900')
frame2.place(x=355, y=380)


label3 = tk.Label(frame2,
                  text='აირჩიეთ სასურველი ვალუტა',
                  bg='#E2FF22',
                  fg='#326939',
                  font=('arial', 13))
label3.pack()


#ტექსტის გამოსატანი(2)
output_label2 = tk.Label(root,
                         text='',
                         font=('arial', 18),
                         fg='#137520',
                         bg='#E2E234')
output_label2.pack(pady=20, padx = 50)


label_where= tk.Label(frame2,text = ('სად'), font = ('arial', 10), bg = '#E2FF22' )
label_where.pack(side = 'right', padx=10)


def button_func10():
   selected_to.set('$')
   output_label2.config(text='თქვენ ყიდულობთ დოლარს')


def button_func20():
   selected_to.set('₾')
   output_label2.config(text='თქვენ ყიდულობთ ლარს')


def button_func30():
   selected_to.set('€')
   output_label2.config(text='თქვენ ყიდულობთ ევროს')


def button_func40():
   selected_to.set('₺')
   output_label2.config(text='თქვენ ყიდულობთ ლირას')



button10 = tk.Button(frame2,
                     text='$',
                     width=2,
                     height=2,
                     font=('bold', 12),
                     bg='#49DE4E',
                     command=button_func10)
button10.pack(side='left', padx=20, pady=2)


button20 = tk.Button(frame2,
                     text='₾',
                     width=2,
                     height=2,
                     font=('bold', 12),
                     bg='#49DE4E',
                     command=button_func20)
button20.pack(side='left', padx=20, pady=2)


button30 = tk.Button(frame2,
                     text='€',
                     width=2,
                     height=2,
                     font=('bold', 12),
                     bg='#49DE4E',
                     command=button_func30)
button30.pack(side='left', padx=20, pady=2)


button40 = tk.Button(frame2,
                     text='₺',
                     width=2,
                     height=2,
                     font=('bold', 12),
                     bg='#49DE4E',
                     command=button_func40)
button40.pack(side='left', padx=20, pady=5)


input1 = tk.Entry(root, width = 15, font = ('arial', 20), bg = '#E3EF97')
input1.place(x= 30 ,y=450)


def convert():
    from_currency = selected_from.get()
    to_currency = selected_to.get()
    amount = input1.get()


    if not from_currency or not to_currency:
        output_label.config(text='აირჩიეთ ვალუტა კონვერტაციისთვის')
        return


    if not amount:
        output_label.config(text='შეიყვანეთ თანხა')
        return

    try:
        amount = float(amount)
    except ValueError:
        output_label.config(text='შეიყვანეთ სწორი თანხა')
        return


    rates = {
        ('₾', '$'): 0.37,
        ('₾', '€'): 0.34,
        ('₾', '₺'): 12.65,
        ('$', '₾'): 2.69,
        ('$', '€'): 0.9,
        ('$', '₺'): 34.04,
        ('€', '₾'): 2.97,
        ('€', '$'): 1.11,
        ('€', '₺'): 37.63,
        ('₺', '₾'): 0.079,
        ('₺', '$'): 0.029,
        ('₺', '€'): 0.027,
        ('₾', '₾'): 1,
        ('$', '$'): 1,
        ('€', '€'): 1,
        ('₺', '₺'): 1
    }

    converted_amount = amount * rates[(from_currency, to_currency)]
    output_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')

button_convert = tk.Button(root, text='კონვერტაცია', bg='#52B917', width=15, height=3, font=('arial', 15),
                               relief='raised', command=convert)
button_convert.place(x=20, y=620)


def cleanup():

    selected_from.set('')
    selected_to.set('')


    input1.delete(0, tk.END)


    output_label.config(text='')
    output_label2.config(text='')


button_cleanup = tk.Button(root, text='გასუფთავება', bg='#ECEC54', fg = '#47453E', width=15, height=2, font=('arial', 11), relief='raised', command=cleanup)
button_cleanup.place(x=540, y=700)

root.mainloop()



















