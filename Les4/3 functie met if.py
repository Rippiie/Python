while True:
    try:
        lengte = int(input("Wat is jou lengte?: "))
        break
    except ValueError:
        print("Voer je lengte in centimeters in.")


