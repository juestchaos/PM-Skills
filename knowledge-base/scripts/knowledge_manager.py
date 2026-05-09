#!/usr/bin/env python3
"""
Knowledge Base Manager for Product Requirements

This script provides functions to retrieve and apply foundational knowledge
when writing product requirements documents.
"""

import os
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path

class KnowledgeBase:
    def __init__(self, knowledge_dir: str = "/home/admin/.openclaw/workspace/references"):
        self.knowledge_dir = knowledge_dir
        self.knowledge_cache = {}
        self.knowledge_order = []  # 保持文件加载顺序
        self._load_knowledge()
    
    def _load_knowledge(self):
        """Load all knowledge files into cache with priority ordering"""
        # 优先级文件列表（置顶）
        priority_files = [
            "/home/admin/.openclaw/workspace/MEMORY.md",
            "/home/admin/.openclaw/workspace/skills/product-manager/SKILL.md",
            "/home/admin/.openclaw/workspace/skills/ui-ux-pro-max/SKILL.md",
        ]
        
        # 1. 先加载优先级文件
        for filepath in priority_files:
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # 使用完整路径作为 key，便于识别来源
                        key = self._generate_key(filepath)
                        self.knowledge_cache[key] = content
                        self.knowledge_order.append(key)
                except Exception as e:
                    print(f"Error loading priority file {filepath}: {e}")
        
        # 2. 加载 references 目录下的其他文件（按修改日期倒排）
        if os.path.exists(self.knowledge_dir):
            other_files = []
            for filename in os.listdir(self.knowledge_dir):
                if filename.endswith('.md') or filename.endswith('.json'):
                    filepath = os.path.join(self.knowledge_dir, filename)
                    # 跳过根目录的测试文件，只处理子目录
                    if os.path.isfile(filepath):
                        try:
                            mtime = os.path.getmtime(filepath)
                            other_files.append((filepath, mtime))
                        except Exception as e:
                            print(f"Error getting mtime for {filepath}: {e}")
            
            # 按修改时间倒序排序
            other_files.sort(key=lambda x: x[1], reverse=True)
            
            # 加载排序后的文件
            for filepath, mtime in other_files:
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        key = self._generate_key(filepath)
                        # 避免重复加载
                        if key not in self.knowledge_cache:
                            self.knowledge_cache[key] = content
                            self.knowledge_order.append(key)
                except Exception as e:
                    print(f"Error loading {filepath}: {e}")
        
        # 3. 递归加载 references 子目录中的文件（按修改日期倒排）
        self._load_subdirectory_knowledge(self.knowledge_dir)
    
    def _generate_key(self, filepath: str) -> str:
        """生成文件的唯一 key，保留路径信息"""
        # 对于优先级文件，使用简化的 key
        if "MEMORY.md" in filepath:
            return "MEMORY"
        elif "product-manager/SKILL.md" in filepath:
            return "product-manager/SKILL"
        elif "ui-ux-pro-max/SKILL.md" in filepath:
            return "ui-ux-pro-max/SKILL"
        else:
            # 其他文件使用相对路径
            rel_path = filepath.replace(self.knowledge_dir + '/', '')
            return rel_path.replace('.md', '').replace('.json', '')
    
    def _load_subdirectory_knowledge(self, base_dir: str):
        """递归加载子目录中的知识文件"""
        if not os.path.exists(base_dir):
            return
        
        subdir_files = []
        for root, dirs, files in os.walk(base_dir):
            # 跳过根目录（已处理）
            if root == base_dir:
                continue
            
            for filename in files:
                if filename.endswith('.md') or filename.endswith('.json'):
                    filepath = os.path.join(root, filename)
                    try:
                        mtime = os.path.getmtime(filepath)
                        subdir_files.append((filepath, mtime))
                    except Exception as e:
                        print(f"Error getting mtime for {filepath}: {e}")
        
        # 按修改时间倒序排序
        subdir_files.sort(key=lambda x: x[1], reverse=True)
        
        # 加载排序后的文件
        for filepath, mtime in subdir_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    key = self._generate_key(filepath)
                    if key not in self.knowledge_cache:
                        self.knowledge_cache[key] = content
                        self.knowledge_order.append(key)
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
    
    def get_knowledge(self, topic: str) -> Optional[str]:
        """Retrieve knowledge by topic name"""
        # Exact match first
        if topic in self.knowledge_cache:
            return self.knowledge_cache[topic]
        
        # Fuzzy match
        for key, content in self.knowledge_cache.items():
            if topic.lower() in key.lower():
                return content
        
        return None
    
    def list_topics(self) -> List[str]:
        """List all available knowledge topics"""
        return list(self.knowledge_cache.keys())
    
    def apply_to_requirements(self, topic: str, requirements_context: str) -> str:
        """Apply knowledge to requirements context"""
        knowledge = self.get_knowledge(topic)
        if not knowledge:
            return requirements_context
        
        # Integrate knowledge into requirements
        integrated = f"""# 基于 {topic} 知识的需求文档

## 基础知识参考
{knowledge}

## 具体需求
{requirements_context}
"""
        return integrated

def main():
    """Command line interface for knowledge base"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python knowledge_manager.py <topic> [context]")
        return
    
    topic = sys.argv[1]
    context = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
    
    kb = KnowledgeBase()
    result = kb.apply_to_requirements(topic, context)
    print(result)

if __name__ == "__main__":
    main()