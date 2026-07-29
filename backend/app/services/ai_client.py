class AIClient:
    PROVIDER_TYPE="unknown"
    def __init__(self,api_key,timeout):
        self.api_key=api_key
        self.timeout=timeout
    def provider_name(self):
        return self.PROVIDER_TYPE
    def call_model(self,prompt):
        return "Base class does not implement model calls"
    
    
class ClaudeClient(AIClient):
    PROVIDER_TYPE="claude"
    def __init__(self,api_key,timeout,model_name):
        self.api_key=api_key
        self.timeout=timeout
        super().__init__(model_name)
        self.model_name=model_name
        
    def provider_name(self):
        return "claude"
    def call_model(self,prompt):
        return "Claude handled the request."
    
class LoggingMixin:
    def log_request(self):
        return "request was logged"
class RetryMixin:
    def retry_request(self):
        return "retry occurred." 
class ClaudeClientWithMiddleware(LoggingMixin,RetryMixin,ClaudeClient):
    pass
