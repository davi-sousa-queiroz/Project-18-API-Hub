# 🚀 Project 18 – API Hub (April 12th - 13th, 2026)

## 💡 Simple Description

A Python terminal app that lets you fetch data from multiple APIs (Pokémon, jokes, and country info) with a clean menu system, while saving user history using JSON.

⸻

## 🧠 The Story

### This project actually started as something small.

I had just learned how to request data from APIs, and I built a few mini projects:
	•	a Pokémon data fetcher
	•	a joke generator
	•	a country info finder

At first, they were all separate. Just random scripts.

But then I thought…
why am I running 3 different files like an NPC?

So I decided to combine everything into one system.

That’s when things got interesting.

Instead of just writing code, I started thinking like:

how do I actually organize this so it doesn’t turn into spaghetti?

⸻

## ⚙️ What the Project Does

### The program runs in the terminal and gives you a menu:
	•	Fetch Pokémon data
	•	Get random jokes
	•	Get country information
	•	View saved history

### Every time you use it:
	•	your searches are saved
	•	your joke count is tracked (very important obviously)
	•	everything persists using a JSON file

⸻

## 🧱 How I Built It

I didn’t just throw everything into one file and pray.

### I structured it like this:
	•	api/ → handles all API requests
	•	utils/menu.py → handles user interaction
	•	utils/file_handler.py → handles JSON saving/loading
	•	utils/history.py → displays stored data
	•	main.py → connects everything together

### I also used:
	•	classes so things don’t get messy
	•	function mapping instead of 500 if statements
	•	JSON as a mini database

⸻

## 🧠 What I Learned

This project felt different.

### I learned how to:
	•	actually use APIs instead of just copying examples
	•	structure multi-file Python projects
	•	separate responsibilities so my code doesn’t become chaos
	•	save and load data properly with JSON

But the biggest thing was:

building something with a lot going on without needing help every 2 minutes

There were moments I got stuck (and yeah, got a little mad at APIs 💀), but figuring things out myself was the best part.

⸻

## 🚀 What’s Next

This project is basically my transition into backend development.

### Next step:
	•	turn this into a real API using Flask
	•	eventually replace JSON with a real database

⸻

## 💬 Final Thoughts

This project was actually fun to build.

### I realized I enjoy this type of work way more when:
	•	there’s structure
	•	there’s problem solving
	•	and I’m not just following a tutorial step by step

Also yeah… APIs can be annoying sometimes 😭

### -Davi 
🧑‍💻❤️
