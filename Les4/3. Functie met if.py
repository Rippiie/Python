while True:
    try:
        lengte = int(input("Wat is jou lengte?: "))
        break
    except ValueError:
        print("Voer je lengte in centimeters in.")
def langGenoeg(x):
    if x >= 120:
        res = 'Je bent lang genoeg voor de attractie!'
    else:
        res = 'Sorry je bent te klein'
    return res
print(langGenoeg(lengte))