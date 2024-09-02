from tracker import WorkoutTracker

def main():
    tracker = WorkoutTracker()

    print("Welcome to the Progressive Overload Tracker!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Record a session")
        print("2. View progress")
        print("3. Show available workout days and exercises")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            tracker.print_options()
            workout_day = input("\nEnter the workout day: ")

            if workout_day not in tracker.workout_days:
                print("Invalid workout day. Try again.")
                continue

            for exercise, details in tracker.workout_days[workout_day].items():
                print(f"\nRecording for {exercise}")
                recommended_weight = tracker.recommend_weight(workout_day, exercise)
                print(f"Recommended weight: {recommended_weight} kg")

                # Prompt for weight
                weight_input = input(f"Enter the weight used for {exercise} (in kg) or type 'skip' to skip: ")
                if weight_input.lower() == "skip":
                    print(f"Skipped {exercise}.")
                    continue

                # Convert weight input if not skipped
                weight = float(weight_input)

                # Prompt for sets
                sets = int(input(f"Enter the number of sets for {exercise}: "))

                # Prompt for reps
                reps = int(input(f"Enter the number of reps per set for {exercise}: "))

                # Record the session
                tracker.record_session(workout_day, exercise, sets, reps, weight)

            print("\nSession recorded successfully!")


        elif choice == "2":
            tracker.print_options()
            workout_day = input("\nEnter the workout day: ")
            exercise = input("Enter the exercise: ")

            progress = tracker.get_progress(workout_day, exercise)

            if progress.empty:
                print(f"No progress recorded yet for {exercise} on {workout_day}.")
            else:
                print(f"\nProgress for {exercise} on {workout_day}:")
                print(progress)

        elif choice == "3":
            tracker.print_options()

        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()