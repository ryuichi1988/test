from pyautogui import pixel
with open ("test002248946.txt","w") as file:
    for x in range (387,499,1):
        for y in range(354,575,1):
            file.write("{},{},rgb{}".format(x,y,pixel(x,y))+"\n")
file.close()