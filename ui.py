import tkinter as tk 
frame = tk.Tk()
frame.title("RariList")
frame.geometry('400x200')

#starting image number input box 
number_of_images_input= tk.Text(frame,height=1,width=5)
number_of_images_input.place(x=150,y=20)

number_of_images_label= tk.Label(frame,text="Number of images:")
number_of_images_label.place(x=40,y=20)

#items amount input box 
items_amount_input = tk.Text(frame,height=1,width=5)
items_amount_input.place(x=150,y=60)
items_amount_label= tk.Label(frame,text="Items amount:")
items_amount_label.place(x=40,y=60)

#royalties amount input box 
royalties_amount_input= tk.Text(frame,height=1,width=5)
royalties_amount_input.place(x=150,y=100)
royalties_amount_label= tk.Label(frame,text="Royalties amount:")
royalties_amount_label.place(x=40,y=100)

#item price input box  
item_price_input = tk.Text(frame,height=1,width=5)
item_price_input.place(x=150,y=140)
item_price_label= tk.Label(frame,text="Item price:")
item_price_label.place(x=40,y=140)

#currency label 
curr = tk.Label(frame,text="ETH")
curr.place(x=200,y=140)

#start button 
start= tk.Button(frame,text="Start listing")
start.place(x=300,y=50)

#Exit button 
exit = tk.Button(frame,text="Exit",command= frame.destroy)
exit.place(x=350,y=160)

frame.mainloop()