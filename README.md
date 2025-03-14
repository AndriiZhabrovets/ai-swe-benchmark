# Artificial Intelligence Benchmarks

## General Idea

The main idea of this project is to assess the current capabilities of various popular artificial intelligence models in the software development field. To achieve this, several benchmarks will be performed on each AI model. More about this in the next section.

## Benchmarks & their Types

Due to the rather wide range of tasks that an average software developer may face during his/her work, it was decided to create several specific categories of benchmarks.

The decision on which categories to use was based on the types of tasks that an average programmer can be asked to solve and on his/her "stats" (efficiency, syntax knowledge, adaptability to new technologies, etc.) that can influence the overall performance of a software engineer. In the end, such categories were formed:

- Data Structure and Algorithm Challenges - problems also known as "technical interview questions" and an essential element of most programming competitions. These types of benchmarks focus mainly on the ability of AI models to write efficient code that can handle heavy test cases without running into execution timeout.
- Debugging - aimed at testing how well AI models can process code written by others.  
- External framework/library usage - forces AI models to use an external library. Observes how well the library's capabilities are used and whether they are used correctly.
- Programming from scratch - tests the ability of AI models to create a simple program given a precise description of how it should work. Rather difficult to benchmark. More research is needed.


## New Idea: AI Evaluation of the result 

Maybe I can implement the usage of AI for evaluation of the results (second layer check):

https://langchain-ai.github.io/langgraph/tutorials/usaco/usaco/

For the implementation of this idea the usage of langchain-ai module is necessary: https://langchain-ai.github.io/langgraph/tutorials/introduction/

## Benchmark Subjects 

Below is a table with the latest information on the most popular AI models that have APIs.

| **AI Model**        | **Company** | **Tiers**                                                                                           | **Pricing**                                                                                                                                                                                                                                                                                                                     | **Languages**            | **Last Updated** | **API/Local** | **Free Tier**                            | **Link**                                |
| ------------------- | ----------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------- | ------------- | ---------------------------------------- | --------------------------------------- |
| **OpenAI GPT**      | OpenAI      | GPT-3.5,<br>GPT-4/GPT-4 Turbo,<br>GPT-4o                                                            | GPT-3.5: $0.002 / 1K tokens, GPT-4: $0.06 / 1K tokens, GPT-4 Turbo: $0.03 / 1K tokens                                                                                                                                                                                                                                           | Python, JavaScript, more | Mar 2024         | API           | Limited access in free tier              | https://platform.openai.com/docs/models |
| **Gemini (Google)** | Google      | Gemini 1.5 Flash,<br>Gemini 1.5 Pro,<br>Gemini 1.0 Pro                                              | Gemini 1.5 Flash: $0.35 / 1 million tokens (for prompts up to 128K tokens), $0.70 / 1 million tokens (for prompts longer than 128K);<br><br>Gemini 1.5 Pro: $3.50 / 1 million tokens (for prompts up to 128K tokens), $7.00 / 1 million tokens (for prompts longer than 128K);<br><br>Gemini 1.0 Pro: $0.50 / 1 million tokens; | Python, JavaScript, more | Jun 2024         | API           | Yes (limited amount of requests per day) | https://ai.google.dev/pricing           |
| **Llama**           | Meta        | Llama 2,<br>Llama 3, Code Llama                                                                     | Free for research and commercial use                                                                                                                                                                                                                                                                                            | Python, C++, more        | July 2024        | Local         | Yes                                      | https://llama.meta.com                  |
| **Claude**          | Anthropic   | Claude 3 Haiku,<br>Claude 3 Opus,<br>Claude 3.5 Sonnet                                              | Pricing per request (API is still in Beta)                                                                                                                                                                                                                                                                                      | Python, JavaScript, more | Apr 2024         | API           | Yes                                      | https://www.anthropic.com/api           |
| **Mistral**         | Mistral AI  | Mistral 7B,<br>Mixtral 8x7B,<br>Mixtral 8x22B,<br>Mistral Small,<br>Mistral Large,<br>Mistral Embed | Pricing not publicly disclosed                                                                                                                                                                                                                                                                                                  | Python, JavaScript, more | Feb 2024         | API           | Yes                                      | https://docs.mistral.ai/api/            |
| **Cohere**          | Cohere      | Command R,<br>Command X,<br>Command XL                                                              | $0.01 - $0.06 / 1k tokens                                                                                                                                                                                                                                                                                                       | PythPython, JavaScript   | July 2024        | API           | Yes                                      | https://cohere.com/command              |


After a careful consideration I've made a decision to stick to only the models from OpenAI, Google and Anthropic.
## Technologies Used

#### The Paper

The Paper is planned to be written in LaTeX, due to its convenience and the freedom of customisation. Other alternatives (Microsoft Word, Google Docs, etc.) can be chosen if the teacher requires to do so.

#### Benchmarks 

The programming language chosen for this project is python. The main reason for this is the fact that based on the table most models have APIs for either Python or Javascript.   

## Benchmark Subjects 
    
The paper will be written in LaTeX because of its convenience and freedom of customisation. Other alternatives (Microsoft Word, Google Docs, etc.) may be used if the teacher so requires.

#### Benchmarks 
    
The programming language selected for this project is Python. This decision was made primarily because, according to the table, the majority of models have APIs for either Python or JavaScript.


## Deadlines and Time Management

The planned deadline for finishing the paper is **the end of the spring holidays**. This will give me enough time to work on it during the summer holidays and then during the autumn ones. Despite the fact that I have a language exchange course, the course itself only takes 3-4 hours in the morning, leaving the rest of the day free for me.

Below is a rough schedule of the work process and possible meetings (to be adjusted with the supervisor):

| **Time**                         | **Task**                                                                                                                                                                                                                                   | **Progress until then**                                                                                                                                                                                                                                                                          | **Status**       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 04.06.2024 or 05.06.2024         | - Discuss possible issues that may arise based on the current plan and structure<br> - The amount of "Samples" can be reduced (taking into account the tiers)                                                                      | General structure established, initial research into different models conducted                                                                                                                                                                                                                        | *to be arranged* |
| Summer Break                     | - Complete the simplest benchmarks ("Algorithm Problems", "Debugging Syntax Errors")<br>- Create problems for the final benchmark (including a prompt for each problem)<br> - *Further tasks may be added following the previous discussion* | - An improved version of the plan is created<br>- Possible difficulties are discussed or potentially resolved                                                                                                                                                                                         | *to be accepted* |
| Week 33 (right after the break)  |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                  | *to be arranged* |
| Week 36 (before lang. exchange)  | - Review of progress (what has been done? what has not been done?)<br>- Discussion of plans for the next few weeks (possibly an online meeting during the language exchange)<br>- Discussion of the whole writing part of the paper                           | - **Best case scenario:** <br>- Benchmarks are complete (only data visualisation and paper writing remain)<br> - **Plan B** (in case some benchmarks appear to be harder to program):<br> - Problems and difficulties of certain benchmarks are defined and prepared for discussion<br> | *to be arranged* |
| Language Exchange + Spring Break | - During the first two weeks, it is necessary to resolve all outstanding issues related to benchmarks (if there are any left)<br>- Organize and represent the results of the benchmarking exercises in a structured and visual manner.<br>- Write the paper                                                      | - **Ideally**: The benchmarks have been completed, and the structure of the paper is now in place, including the outline and table of contents                                                                                                                                                                                   | *to be accepted* |
| Week 43 (right after the break)  | - Submitting the paper **OR** Final review of the entire paper                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                  | *to be arranged* |

## Possible difficulties

- The use of free models may not be sufficient to provide a more realistic overview. The cost of this project may therefore be an issue.
    - Possible solution: Use the free tier models for general benchmarking, then test more powerful models.
- Debugging revolves around solving different types of errors (bugs), some are syntax errors that make the benchmark possible, but there are also logical and functional errors that do not cause an error in the compiler. The code runs but does not produce the expected result. 
	- Note: The benchmark could also be possible in such cases, but the command given to the AI model would have to be specific to each problem.
	- Possible solution: Debugging benchmarks can be divided into two categories: Syntax and Logic problem solving. This way two different abilities of AI models can be tested:
		- The ability to find syntax errors (which can be compared to sitting with documentation and simply checking that everything is done according to the rules).
		- The ability to solve logic errors (which requires an "idea" of how a final product should work).
	- Additional problem: Sometimes syntax errors are not just typos or forgotten characters, some syntax errors may also require logical thinking.
- There is still no idea how to create "programming from scratch" type benchmarks.
- The Claude AI API is still in beta, so there may be difficulties in using it.
