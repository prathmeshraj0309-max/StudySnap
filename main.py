notes = {}

while True:

    print("\n=================================")
    print("          STUDYSNAP")
    print("=================================")

    print("\nStudy Smarter. Learn Faster.\n")

    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Quiz Mode")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # ADD NOTE
    if choice == "1":

        subject = input("Enter Subject: ")
        note = input("Enter Note: ")

        if subject in notes:
            notes[subject].append(note)
        else:
            notes[subject] = [note]

        print("Note added successfully!")

    # VIEW NOTES
    elif choice == "2":

        if len(notes) == 0:
            print("No notes available!")

        else:
            print("\n===== YOUR NOTES =====\n")

            for subject, note_list in notes.items():

                print(subject)
                print("-" * len(subject))

                for i, note in enumerate(note_list, start=1):
                    print(f"{i}. {note}")

                print()

    # SEARCH NOTES
    elif choice == "3":

        search_subject = input("Enter Subject: ")

        if search_subject in notes:

            print(f"\n{search_subject} Notes")
            print("-" * (len(search_subject) + 6))

            for i, note in enumerate(notes[search_subject], start=1):
                print(f"{i}. {note}")

        else:
            print("No notes found!")

    # QUIZ MODE
    elif choice == "4":

        subject = input("Enter Subject: ")

        if subject in notes:

            print(f"\nQuiz Mode - {subject}")

            for note in notes[subject]:

                print("\nQuestion:")
                print("Explain:")
                print(note)

                input("\nPress Enter to reveal answer...")

                print("Answer:")
                print(note)

        else:
            print("No notes available for this subject!")

    # EXIT
    elif choice == "5":

        print("\nThank you for using StudySnap!")
        break

    # INVALID INPUT
    else:

        print("Invalid Choice! Please try again.")