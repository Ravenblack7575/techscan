# TECHSCAN
A prototype Multi-Agent Research Assistant using Crew AI

### What is this project about?

**TechScan** is a prototype exploring the use of **multi-agent AI for tech news scanning and literature review**. Its core mission is to help researchers stay informed about the latest advancements in science and technology by tackling the challenge of information overload, particularly in cross-discipline fields.

<img width="968" height="454" alt="Screenshot 2025-10-31 160420" src="https://github.com/user-attachments/assets/caf951e6-d706-43ac-a5d5-92d96b0e6b06" />

This agentic AI system autonomously searches the internet for recent news, product releases, and research findings, analyzes emerging trends, and generates **concise summary reports**. Built using Python and the crewAI framework, TechScan employs a crew of four agents: a **Tech News Researcher** (to gather information), a **Tech Consultant/Advisor** (to evaluate findings and identify trends), a **Tech Writer** (to produce the summary report), and a **Tech Report Editor** (to ensure clarity and consistency).

The resulting report provides a quick overview, offers initial topic sensing, and recommends directions for research and development. The prototype utilized a local Large Language Model (LLM) to offer advantages in security, confidentiality, and lower operational cost.

(This project summary is generated using NotebookLM)

### Libraries used

Poetry was used to manage the python modules.

This project uses CrewAI (and CrewAI tools) to create the agents and manage them. (Love the simplicity of CrewAI.)

SerperAPI is used to access google search for web searches. (I'll probably try DuckDuckGo next time, because Serper will cost money.)

LLM is accessed using LM Studio and the model applied here is Gemma-3n-E4B-it-text-GGUF. (In future version (if any) I think that I might try DeepSeek for the reasoning parts, and Gemma for the writing.)


### How to run it

This agentic system currently runs off jupyter notebook. An additional config file contains the required connections to local LLM server (LM Studio) with the required models and api call to SerperAPI for performing google search. A separate file containing API keys is required (which is not uploaded here).

</BR>
</BR>

### Thoughts 

It was satisfying to make this even though I can't say that it was successful. Obviously it's a try by a complete newbie. It was interestng and cool to see the AI agents working. 

I suspect many websites don't allow scraping, as such the information retrieved was limited to what the agent is allow to read or scrape. I suspect much of the generated text is produced from hallucinations. So I do need to implement some method of evaluation on the next round.

One could get better results with bigger models. LLMs are getting better and they have costs attached to them. 

Elizabeth Lim 2025



