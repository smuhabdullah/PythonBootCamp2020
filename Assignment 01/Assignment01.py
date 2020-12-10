"""Python Boot Camp 2020 Assignment Number 01"""
# Q No 1
def diagonal(name):
    for i in range(len(name)):
        print( " "*i + name[i])

# Q No 2

def ClassRoom(record):
    dict = {}
    i = 0
    while i < record:
        print()
        roll_num = input(f"Enter your {i+1}th roll number: ")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        marks = int(input("Enter your marks(out of 100): "))
        dict[roll_num] = [name,age,marks] 
        if marks > 100 or marks < 0:
            print("Please Enter the marks out of 100")
            del dict[roll_num]
            i = (i+1) - 1
        else:
            i = i + 1

    print()
    print("Roll_num | Name | Age | marks(out of 100)")
    total = 0
    num = []

    for j in dict:
        print(f"""{j}\t   {str(dict[j][0])}  \t{str(dict[j][1])}\t{str(dict[j][2])}""")
        
        total+=dict[j][2]
        num.append(dict[j][2])
        

    avg = total / record
    high = max(num)
    low = min(num)

    return(f"""
class average is {avg}
class highest is {high}
class lowest is {low}""")



# Q3
song = f"""They look for picture perfect
Don't look deeper than the surface
Bubblegum always pops and
Stars they fade out, life never stops
I don't do what Simon says
Get the message 'cause it's read
That's just life it never plays fair
Said to follow any dream
Be a puppet on a string
Works for you but that isn't me
This ain't another pop song 'bout fallin' in love
Or a party song 'bout drinks and drugs
No more singin' songs 'bout breakin' my heart
And my lonely nights, dancin' in the dark
If I'm a guilty pleasure
I want this life forever
I'll take it on 'cause anything is better
Than another pop song 'bout fallin' in love
But if you wanna sing along say, "I don't give a what"
A hamster on the wheel
That's how it's feels tryin' to be real
These unrealistic expectations,…
I don't do what Simon says
Get the message 'cause it's read
That's just life it never plays fair
Said to follow any dream
Be a puppet on a string"""
import time
def lyrics(song):
    x = song.split("\n")
    for i in x:
        print(i)
        delay = 1
        time.sleep(delay)


if __name__ == "__main__":

    # Q1
    name = input("Name is : ")
    diagonal(name)

    # Q2
    x = ClassRoom(5)
    print(x)
    
    # Q3
    lyrics(song)
