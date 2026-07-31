from app.ai.providers import ProviderFactory

from app.ai.agents.resume_agent import ResumeAgent
from app.ai.agents.ats_agent import ATSAgent
from app.ai.agents.placement_agent import PlacementAgent
from app.ai.agents.salary_agent import SalaryAgent
from app.ai.agents.career_agent import CareerAgent
from app.ai.agents.interview_agent import InterviewAgent
from app.ai.agents.resume_optimizer_agent import ResumeOptimizerAgent
from app.ai.agents.resume_builder_agent import ResumeBuilderAgent
from app.ai.agents.job_matching_agent import JobMatchingAgent


class AgentFactory:

    @staticmethod
    def _provider():
        return ProviderFactory.create()

    @staticmethod
    def resume():
        return ResumeAgent(AgentFactory._provider())

    @staticmethod
    def ats():
        return ATSAgent(AgentFactory._provider())

    @staticmethod
    def placement():
        return PlacementAgent(AgentFactory._provider())

    @staticmethod
    def salary():
        return SalaryAgent(AgentFactory._provider())

    @staticmethod
    def career():
        return CareerAgent(AgentFactory._provider())

    @staticmethod
    def interview():
        return InterviewAgent(AgentFactory._provider())

    @staticmethod
    def resume_optimizer():
        return ResumeOptimizerAgent(AgentFactory._provider())

    @staticmethod
    def resume_builder():
        return ResumeBuilderAgent(AgentFactory._provider())

    @staticmethod
    def job_matching():
        return JobMatchingAgent(AgentFactory._provider())