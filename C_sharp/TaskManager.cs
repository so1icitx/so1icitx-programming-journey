using System;
using System.Collections.Generic;

namespace TaskManager
{
    class Task
    {
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
        public DateTime CreatedAt { get; set; }

        public Task(string description)
        {
            Description = description;
            IsCompleted = false;
            CreatedAt = DateTime.Now;
        }

        public override string ToString()
        {
            return $"[{CreatedAt:yyyy-MM-dd HH:mm}] {Description} ({(IsCompleted ? "Completed" : "Pending")})";
        }
    }

    class Program
    {
        static List<Task> tasks = new List<Task>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\nTask Manager");
                Console.WriteLine("1. Add Task");
                Console.WriteLine("2. List Tasks");
                Console.WriteLine("3. Mark Task as Completed");
                Console.WriteLine("4. Exit");
                Console.Write("Choose an option: ");

                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        AddTask();
                        break;
                    case "2":
                        ListTasks();
                        break;
                    case "3":
                        MarkTaskCompleted();
                        break;
                    case "4":
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Invalid option. Try again.");
                        break;
                }
            }
        }

        static void AddTask()
        {
            Console.Write("Enter task description: ");
            string description = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(description))
            {
                tasks.Add(new Task(description));
                Console.WriteLine("Task added successfully.");
            }
            else
            {
                Console.WriteLine("Description cannot be empty.");
            }
        }

        static void ListTasks()
        {
            if (tasks.Count == 0)
            {
                Console.WriteLine("No tasks available.");
                return;
            }
            for (int i = 0; i < tasks.Count; i++)
            {
                Console.WriteLine($"[{i + 1}] {tasks[i]}");
            }
        }

        static void MarkTaskCompleted()
        {
            ListTasks();
            Console.Write("Enter task number to mark as completed: ");
            if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= tasks.Count)
            {
                tasks[index - 1].IsCompleted = true;
                Console.WriteLine("Task marked as completed.");
            }
            else
            {
                Console.WriteLine("Invalid task number.");
            }
        }
    }
}
