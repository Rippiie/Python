while True:
    try:
        lengte = int(input("Wat is jou lengte?: "))
    except ValueError:
        print("Voer je lengte in centimeters in.")
    else:
        break

