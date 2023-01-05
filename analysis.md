Products :
    Product:
    -name
    -sku
    -brand
    -price
    -dicriptions
    -tags
    -weight
    -category
    -flag : new , feature

    Brand:
        -name
    Category:
        -name
        -image

    Reviews:
        -product
        -user
        -review
        -rate
        -created_at

    images:
        -product
        -image

    Order:
        Orders:
            -id
            -order_status [Recieved , Processed , Shipped , Delivered]
            -order time
            -delivery time
            -sub total
            -discount
            -delivery fee
            -total
            -delivery location
        OrdersDetails:
            -serial
            -order
            -product
            -price
            -quantity


    Users:
        Profile
            -name
            -email
            -image
        User phone number
            -user
            -phone_number
            -type
        User Address
            -user
            -address
            -title

    Coupons & Offer :
