# Artificial Intelligence Benchmark
- [[#General Idea|General Idea]]
- [[#Benchmarks & their Types|Benchmarks & their Types]]
- [[#Benchmark Subjects|Benchmark Subjects]]
- [[#Technologies Used|Technologies Used]]
		- [[#The Paper|The Paper]]
		- [[#Benchmarks|Benchmarks]]
- [[#Deadlines and Time Management|Deadlines and Time Management]]
- [[#Possible difficulties|Possible difficulties]]

## General Idea

The main idea of this project is to asses the current capabilities of various popular Artificial Intelligence models in the sphere of software development. In order to do so, several benchmarks will be performed on each AI model. More about it in the next section.

## Benchmarks & their Types

Due to a rather broad spectre of task which an average software developer can face during his/her work, it was decided to create several special categories of benchmarks.

The decision of which categories will be used was based on the types of tasks an average programmer can be required to solve and his/her "stats" (efficiency, syntax knowledge, adaptability to new technologies, etc.) that can influence the overall performace of a software engineer. In the end such categories have been formed:

- Data structure and algorithm challenges – problems that are also know as "Technical interview questions" and an essential element of most Programming Olympiads. These types of benchmarks concentrate mostly on the capability of AI models to write efficient code, which can handle processing heavy test cases without running into execution timeout.
- Debugging – aimed towards testing how well can AI models process the code written by others.  
- External framework/library usage – forces AI models to use an external library. Observation how well the capabilities of the libraries are used and if they are even used correct.
- Programming from Scratch – tests the ability of AI models to create a simple program given a precise description of how it is supposed to function. Rather difficult to create a benchmark. Further research is required.


## Benchmark Subjects 

Below is a table with the latest information on the most popular AI models which have APIs.  

| **AI Model**        | **Company** | **Tiers**                                                                                           | **Pricing**                                                                                                                                                                                                                                                                                                                     | **Languages**            | **Last Updated** | **API/Local** | **Free Tier**                            | **Link**                                |
| ------------------- | ----------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------- | ------------- | ---------------------------------------- | --------------------------------------- |
| **OpenAI GPT**      | OpenAI      | GPT-3.5,<br>GPT-4/GPT-4 Turbo,<br>GPT-4o                                                            | GPT-3.5: $0.002 / 1K tokens, GPT-4: $0.06 / 1K tokens, GPT-4 Turbo: $0.03 / 1K tokens                                                                                                                                                                                                                                           | Python, JavaScript, more | Mar 2024         | API           | Limited access in free tier              | https://platform.openai.com/docs/models |
| **Gemini (Google)** | Google      | Gemini 1.5 Flash,<br>Gemini 1.5 Pro,<br>Gemini 1.0 Pro                                              | Gemini 1.5 Flash: $0.35 / 1 million tokens (for prompts up to 128K tokens), $0.70 / 1 million tokens (for prompts longer than 128K);<br><br>Gemini 1.5 Pro: $3.50 / 1 million tokens (for prompts up to 128K tokens), $7.00 / 1 million tokens (for prompts longer than 128K);<br><br>Gemini 1.0 Pro: $0.50 / 1 million tokens; | Python, JavaScript, more | Jun 2024         | API           | Yes (limited amount of requests per day) | https://ai.google.dev/pricing           |
| **Llama**           | Meta        | Llama 2,<br>Llama 3, Code Llama                                                                     | Free for research and commercial use                                                                                                                                                                                                                                                                                            | Python, C++, more        | July 2024        | Local         | Yes                                      | https://llama.meta.com                  |
| **Claude**          | Anthropic   | Claude 3 Haiku,<br>Claude 3 Opus,<br>Claude 3.5 Sonnet                                              | Pricing per request (API is still in Beta)                                                                                                                                                                                                                                                                                      | Python, JavaScript, more | Apr 2024         | API           | Yes                                      | https://www.anthropic.com/api           |
| **Mistral**         | Mistral AI  | Mistral 7B,<br>Mixtral 8x7B,<br>Mixtral 8x22B,<br>Mistral Small,<br>Mistral Large,<br>Mistral Embed | Pricing not publicly disclosed                                                                                                                                                                                                                                                                                                  | Python, JavaScript, more | Feb 2024         | API           | Yes                                      | https://docs.mistral.ai/api/            |
| **Cohere**          | Cohere      | Command R,<br>Command X,<br>Command XL                                                              | $0.01 - $0.06 / 1k tokens                                                                                                                                                                                                                                                                                                       | PythPython, JavaScript   | July 2024        | API           | Yes                                      | https://cohere.com/command              |

## Technologies Used

#### The Paper
    
The Paper is planned to be written in LaTeX, due to its convenience and the freedom of customisation. Other alternatives (Microsoft Word, Google Docs, etc.) can be chosen if the teacher requires to do so.

#### Benchmarks 
    
The programming language chosen for this project is Python. The main reason for this is the fact that based on the table most models have APIs for either Python or Javascript.   


## Deadlines and Time Management

The planned deadline for finishing the paper is **the end of the autumn break**. This way I will have enough time to work on it during the summer break and afterwards during the autumn break. Despite the fact that I do have a language exchange program, the programm itself takes only 3-4 hours in the morning with the rest of the day free for my usage.

Below is showed a rough plan of the working process and the possible meetings (has to be ajusted with the supervisor):

| **Time**                         | **Task**                                                                                                                                                                                                                                   | **Progress until then**                                                                                                                                                                                                                                                                          | **Status**       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 04.06.2024 or 05.06.2024         | - Discussion of possible issues that can come up based on the current plan and structure<br> - The amount of "Samples" can be reduces (taking into account the tiers)                                                                      | General structure created, initial research of the various models is done                                                                                                                                                                                                                        | *to be arranged* |
| Summer Break                     | - Finish simplest benchmarks ("Algorithm Problems", "Debugging of syntax errors")<br>- Create problems for the final benchmark (including a prompt for each of the problem)<br> - *Other tasks can be added after the previous discussion* | - Improved version of the plan is created<br>- Possible difficulties are discussed or potentially solved                                                                                                                                                                                         | *to be accepted* |
| Week 33 (right after the break)  |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                  | *to be arranged* |
| Week 36 (before lang. exchange)  | - Checking of the progress (What is done? What is not? )<br>- Discussion of the plans for the next weeks (maybe a possible online meeting during lang. exchange)<br>- Discussion of the whole paper writing part                           | - **Best case scenario:** <br>- Benchmarks are completed (only data visualisation, paper writing is left)<br> - **Plan B** (in case some benchmarks appear to be harder to programm):<br> - Problems and difficulties of certain benchmarks are defined and are prepared for being discussed<br> | *to be arranged* |
| Language Exchange + Spring Break | - Solve all the problems left with benchmarks during the first two weeks (if there are still any left)<br>- Organise and visualise the results of the benchmarks<br>- Write the paper                                                      | - **Ideally**: Benchmarks are done<br>- The structure of the paper is created (the outline, table of contents)                                                                                                                                                                                   | *to be accepted* |
| Week 43 (right after the break)  | - Give-in of the paper **OR** the final review of the whole paper                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                  | *to be arranged* |

## Possible difficulties

- In order to get a more realistic overview, the usage of free models can be considered not sufficient enough. Thus the expences of this project may come up as an issue.
    - Possible solution: Use the free tier models for the general benchmark creation, then test more powerful models.
- Debugging revolves around solving different types of errors (bugs), some are syntax errors, with which the benchmark is possible, but there are also logical and functional errors, which do not cause any error in the compiler. The code runs, but it does not give an expected result. 
	- Note: The benchmark could be possible in such cases as well the command given to the AI model would have to be special for each problem.
	- Possible solution: Debugging benchmarks can be divided into two categories: Syntax and Logic problem solving. This way two different abilities of AI models can be tested:
		- Ability to find syntax errors (which can be compared to sitting with a documentation and simply checking if everything is done according to the rules).
		- Ability to solve logic errors (which requires an "idea" of how a final product is supposed to function)
	- Additional Issue: Sometimes Syntax errors are not just typos or forgotten characters, some syntax erros can also require logical thinking.
- There is still no idea how to create "Programming from scratch" type of benchmarks.
- Claude AI API is still in Beta, because of that the difficulties with its usage may appear.
