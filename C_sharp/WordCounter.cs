using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace WordCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 1)
            {
                Console.WriteLine("Usage: WordCounter <file_path>");
                Environment.Exit(1);
            }

            string filePath = args[0];
            try
            {
                var stats = CountWords(filePath);
                PrintStatistics(stats);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Environment.Exit(1);
            }
        }

        static Dictionary<string, int> CountWords(string filePath)
        {
            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException($"File '{filePath}' not found.");
            }

            string content = File.ReadAllText(filePath);
            char[] separators = { ' ', '\n', '\r', '\t', '.', ',', '!', '?' };
            var words = content.Split(separators, StringSplitOptions.RemoveEmptyEntries)
                              .Select(word => word.ToLower().Trim())
                              .Where(word => !string.IsNullOrEmpty(word));

            var wordCounts = new Dictionary<string, int>();
            foreach (var word in words)
            {
                if (wordCounts.ContainsKey(word))
                {
                    wordCounts[word]++;
                }
                else
                {
                    wordCounts[word] = 1;
                }
            }

            return wordCounts;
        }

        static void PrintStatistics(Dictionary<string, int> wordCounts)
        {
            Console.WriteLine($"Total unique words: {wordCounts.Count}");
            Console.WriteLine($"Total word count: {wordCounts.Values.Sum()}");
            Console.WriteLine("\nTop 5 most frequent words:");
            var topWords = wordCounts.OrderByDescending(kvp => kvp.Value)
                                    .Take(5);
            foreach (var kvp in topWords)
            {
                Console.WriteLine($"Word: {kvp.Key}, Count: {kvp.Value}");
            }
        }
    }
}
