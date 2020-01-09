"""
HOW DOES IT WORK ? / NASIL ÇALIŞIR ?

The administration will place the students into groups based on the Fall Semester averages of all MTs, PG,
& AQs (in proportion with their weight in the Yearly Achievement Grade).


FUNCTION = (MT average X 0.625 + PG average X 0.25 + AQ average x 0.125)

MT = MID TERM
PG = PERFORMANCE GRADE (consist of POP-QUIZ and IG)
AQ = ANNOUNCED QUIZ


"""


def aritmethic_eng ( ) :
    input_string = input( "Enter a list numbers or elements separated by space: " )
    userList = input_string.split()
    print( "user list is " , userList )

    print( "Calculating sum of element of input list" )
    sum = 0
    for num in userList :
        sum += int( num )
    print( "Sum = " , sum )
    arit = sum / len( userList )
    print( "Number of notes you entered :" , len( userList ) )
    print( f"Average of the Notes You Enter: {arit}" )
    return arit


def aritmethic_tr ( ) :
    input_string = input( "Boşluk bırakarak notlarınızı giriniz: " )
    userList = input_string.split()
    print( "Girdiğiniz notların listesi " , userList )

    print( "Notlarınız toplanıyor ... " )
    sum = 0
    for num in userList :
        sum += int( num )
    print( "Toplamı = " , sum )
    arit = sum / len( userList )
    print( "Girdiğiniz Not Adedi :" , len( userList ) )
    print( f"Girdiğiniz Notların Ortalaması: {arit}" )
    return arit


def overall_aritmechic_eng ( ) :
    print( "MID-TERM  \n" )
    a = aritmethic_eng()

    print( "ANNOUNCED QUIZ \n" )
    b = aritmethic_eng()

    print( "PERFORMANCE GRADES (Pop-Quizs (PQ) ve Instructor Grades (IG) \n" )
    c = aritmethic_eng()

    finish = (a * 0.625) + (b * 0.125) + (c * 0.25)

    print( f"\n\n****************************\n Your total average : {finish} " )


def overall_aritmechic_tr ( ) :
    print( "MID-TERM  \n" )
    a = aritmethic_tr()

    print( "ANNOUNCED QUIZ \n" )
    b = aritmethic_tr()

    print( "PERFORMANCE GRADES (Pop-Quiz leri (PQ) ve Instructor Grade leri (IG) \n" )
    c = aritmethic_tr()

    finish = (a * 0.625) + (b * 0.125) + (c * 0.25)

    print( f"\n\n****************************\n Genel ortalamanız  : {finish} " )


print( "DBE GRADE CALCULATOR | WELCOME / HOŞGELDİNİZ\n 1. ENGLİSH\n 2.TÜRKÇE" )
lan = int( input( "PLEASE SELECT LANGUAGE / LÜTFEN DİL SEÇİNİZ :  " ) )
while True :
    if lan == 1 :
        overall_aritmechic_eng()
    elif lan == 2 :
        overall_aritmechic_tr()
    else :
        print( "Lütfen 1 veya 2 dışında herhangi bir şey tuşlamayınız" )
    break
