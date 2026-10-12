#count the total possible number of notes in the user given amount
total_amount = int(input("ENTER THE AMOUNT YOU'VE:: ")) #rupee
note_500 = total_amount // 500
total_amount %= 500
note_200 = total_amount // 200
total_amount %= 200
note_100 = total_amount // 100
total_amount %= 100
note_50 = total_amount // 50
total_amount %= 50
note_10 = total_amount // 10
total_amount %= 10
coin_5 = total_amount // 5
total_amount %= 5
coin_1 = total_amount // 1
total_amount %= 1
print("Total notes&coins:: ",note_500 + note_200 + note_100 + note_50 + note_10 + coin_5 + coin_1)


