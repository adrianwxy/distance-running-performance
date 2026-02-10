from datetime import datetime
from memory import recall_past_analyses

class RunAnalysisChat:
    def __init__(self, llm, collection, system_prompt: str):
        today_str = datetime.now().strftime("%B %d, %Y")
        self.llm = llm
        self.collection = collection
        self.system_prompt = f"Today's date is {today_str}.\n{system_prompt}"
        self.history = []


    def ask(self, user_message: str) -> str:


        past_summaries = recall_past_analyses(self.collection, user_message, days_ago=30)
        
        self.history.append(f"User: {user_message}")

        full_prompt = self._build_prompt(past_summaries) 
        
        response = self.llm.generate(full_prompt)

        self.history.append(f"Assistant: {response}")
        return response


    def _build_prompt(self, long_term_memories: list) -> str:
        conversation = "\n".join(self.history)


        if long_term_memories:
            memory_text = "\n".join(long_term_memories)
            context_header = f"### YOUR PREVIOUS ANALYSES:\n{memory_text}"
        else:
            context_header = ""

            
        return f"""
        {self.system_prompt}
        
        {context_header}
        
        ### CURRENT CONVERSATION:
        {conversation}
        
        Respond as a thoughtful and experienced running coach. 
        If past context is provided, use it to ensure continuity in training.
        """

