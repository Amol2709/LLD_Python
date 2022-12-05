## Requirements:

operation:
1. insertCard
2. Return Money (withDraw)
3. Calculate Money
4. Change Pin
5. Generate Pin
6. Display Remaining Balance
7. Enter Pin
8. Check balance
9. Enter Amount


Entities/Objects:
1. ATM Card
2. Display Board
3. NumberPlate
4. CardEntryPoint
5. CashDispenseSection
6. ATM Machine
7. User


Flow:

1. User Need to insert ATM card
2. User Need to select any one operation 
3. User Need Enter RequireDetails
4. Based on operation : ATM will perform Task
    Example:
            a. Pin Generation
            b. Cash WithDrawn
            c. Check Balance
            ...
            ...
            etc


State:
1. Idle:
    AcceptCard

2. HasCard
    SelectOperation

3. CheckBalance
4. CashWithDrawn



Solution: Try to apply chain of responsibilty and State Pattern



### Future Requiremnt:

1. Transaction should happen without ATM card (YONO)