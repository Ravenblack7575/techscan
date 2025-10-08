# techscan
Multi-Agent Research Assistant

### What is this project about?

**TechScan** is a prototype exploring the use of **multi-agent AI for tech news scanning and literature review**. Its core mission is to help researchers stay informed about the latest advancements in science and technology by tackling the challenge of information overload, particularly in cross-discipline fields.

This agentic AI system autonomously searches the internet for recent news, product releases, and research findings, analyzes emerging trends, and generates **concise summary reports**. Built using Python and the crewAI framework, TechScan employs a crew of four agents: a **Tech News Researcher** (to gather information), a **Tech Consultant/Advisor** (to evaluate findings and identify trends), a **Tech Writer** (to produce the summary report), and a **Tech Report Editor** (to ensure clarity and consistency).

The resulting report provides a quick overview, offers initial topic sensing, and recommends directions for research and development. The prototype utilized a local Large Language Model (LLM) to offer advantages in security, confidentiality, and lower operational cost.

### Libraries used

Poetry is used to manage the python modules.

This project uses CrewAI (and CrewAI tools) to create the agents and manage them. (Love the simplicity of CrewAI.)

SerperAPI is used to access google search for web searches. (I'll probably try DuckDuckGo next time, because Serper will cost money.)

LLM is accessed using LM Studio and the model applied here is Gemma-3n-E4B-it-text-GGUF. (Deep Seek may be a better LLM for the reasoning parts, Gemma may be better for the writing.)

</BR>

### Thoughts 

It was satisfying to see it work but what I learned doing this grounds me a bit. There's a cost to running LLMs even locally, in terms of computing power which translates to electricity and carbon costs. Google search via SERPER was not free, and I suspect many websites don't allow scraping, as such the information retrieved was limited to what the agent is allow to read or scrape. One could get better results with bigger models but again LLMs are not completely free. 


