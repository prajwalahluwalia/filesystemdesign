from models.document import Document
from models.user import User

user = User()

if __name__=="__main__":
    instructions = [
        "add xyz.txt testDocument []",
        "share [a,b,c] testDocument",
        "share [a,b,c] testDocument1",
        "remove [c] testDocument",
        "delete testDocument"
    ]

    for instruction in instructions:
        instruct = instruction.split(" ") 
        # [add. xyz.txt, textDocument]
        print(instruct)
        if instruct[0]=="add":
            if len(instruct)<3:
                print(f"Plese provide correct input for {instruct[0]} operation.")
            print(user.addUserDocument(instruct[1], instruct[2], instruct[3]))
        
        elif instruct[0]=="share":
            if len(instruct)<3:
                print(f"Plese provide correct input for {instruct[0]} operation.")

            print(user.addAccessToDocument(instruct[1], instruct[2]))

        elif instruct[0]=="remove":
            if len(instruct)<3:
                print(f"Plese provide correct input for {instruct[0]} operation.")

            print(user.removeAccessFromDocument(instruct[1], instruct[2]))

        elif instruct[0]=="delete":
            if len(instruct)<2:
                print(f"Plese provide correct input for {instruct[0]} operation.")

            print(user.deleteDocument(instruct[1]))

        else:
            print(f"Incorrect intruction defined.")