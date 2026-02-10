from datetime import datetime, timedelta

def commit_session_to_memory(collection, session_summary, keywords):
 
    now = datetime.now()
    today_str = now.strftime("%Y%m%d")
    readable_date = now.strftime("%B %d, %Y")

    dated_summary = f"Date: {readable_date}\nSummary: {session_summary}"
    existing_today = collection.get(where={"date_id": int(today_str)})

    session_count = len(existing_today['ids']) + 1
    session_id = f"{today_str}_{session_count}"
    
    collection.add(
        documents=[dated_summary],
        ids=[session_id],
        metadatas=[{
            "date_id": int(today_str), 
            "timestamp": now.isoformat(),
            "keywords": ", ".join(keywords),
            "type": "session_analysis"
        }]
    )
    
    print(f" Session {session_id} committed.")
    return session_id




def recall_past_analyses(collection, query_text, days_ago=30):
    threshold = int(
        (datetime.now() - timedelta(days=days_ago)).strftime("%Y%m%d")
    )

    results = collection.query(
        query_texts=[query_text],
        n_results=3,
        where={"date_id": {"$gte": threshold}},
        include=['documents', 'metadatas', 'distances'] 
    )

    
    if not results or not results['documents'][0]:
        return []

    memories = results['documents'][0]
    metadatas = results['metadatas'][0]
    distances = results['distances'][0]
    
    extracted = []
    for m, meta, dist in zip(memories, metadatas, distances):
        if dist < 1.0:
            extracted.append({
                "date": meta['date_id'],
                "content": m
            })

    extracted.sort(key=lambda x: x['date'])

    

    return results["documents"][0] if results["documents"] else []
