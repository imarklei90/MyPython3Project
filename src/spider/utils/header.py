# coding: utf-8

from . import user_agents
import random


def get_user_agent():
    """
        从user_agents字典中随机选择一个user_agent
    """
    # 从非空序列中随机选择一个元素
    return random.choice(user_agents)