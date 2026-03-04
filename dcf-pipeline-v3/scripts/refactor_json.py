import os
import re
from pathlib import Path

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        
        # Replace occurrences in SKILL.md templates
        # ```json \n { \n ... \n } \n -->
        # to
        # ```json \n { \n ... \n } \n ```
        
        content = re.sub(
            r'<!--\s*JSON_PAYLOAD\s*\n\s*(\{.*?\})\s*\n\s*-->',
            r'```json\n\1\n```',
            content,
            flags=re.DOTALL
        )
        
        # Replace inline mentions of ```json
        content = content.replace("```json", "```json")
        content = content.replace("```json", '```json')
        content = content.replace("```json", '```json') # just in case
        
        # Specific fix for validate_compliance.py regex
        content = content.replace(r'"regex": r"```json",', r'"regex": r"```json",')
        content = content.replace(r're.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)', r're.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)')
        content = content.replace(r'"desc": "Bloco ```json exportado",', r'"desc": "Bloco ```json exportado",')

        # Specific fix for fallback_repair.py strings
        content = content.replace('"Bloco ```json exportado":', '"Bloco ```json exportado":')
        
        # Remove trailing --> that might be left orphaned if replacing line by line
        # but the re.sub with DOTALL should have caught the multiline blocks
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    repo_dir = r"c:\Users\T-Gamer\Documents\GitHub\dfc\dcf-pipeline-v3"
    
    for root, dirs, files in os.walk(repo_dir):
        if '.git' in root or '.system_generated' in root:
            continue
        for file in files:
            if file.endswith('.md') or file.endswith('.py') or file.endswith('.json'):
                replace_in_file(os.path.join(root, file))
