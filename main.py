from tracker import WorkoutTracker

def main():
    tracker = WorkoutTracker()

    print("Welcome to the Progressive Overload Tracker!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Record a session")
        print("2. View progress")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            workout_day = input("Enter the workout day (Leg Day, Shoulder Day, Back Day, Bicep_Tricep Day, Glute Day): ")

            if workout_day not in tracker.workout_days:
                print("Invalid workout day. Try again.")
                continue

            for exercise, details in tracker.workout_days[workout_day].items():
                print(f"\nRecording for {exercise}")
                recommended_weight = tracker.recommend_weight(workout_day, exercise)
                print(f"Recommended weight: {recommended_weight} kg")

                weight = float(input(f"Enter the weight used for {exercise} (in kg): "))
                sets = details["sets"]
                reps = details["reps"]

                tracker.record_session(workout_day, exercise, sets, reps, weight)

            print("\nSession recorded successfully!")

        elif choice == "2":
            workout_day = input("Enter the workout day: ")
            exercise = input("Enter the exercise: ")

            progress = tracker.get_progress(workout_day, exercise)

            if progress.empty:
                print(f"No progress recorded yet for {exercise} on {workout_day}.")
            else:
                print(f"\nProgress for {exercise} on {workout_day}:")
                print(progress)

        elif choice == "3":
            print("Exiting the tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

