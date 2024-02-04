from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from magicai.forms import UserPromptForm
from magicai.models import ResponseData, UserPrompt
from magicai.openai_client import OpenAiClient


class UserPromptView(CreateView):
    template_name = "magicai/user_prompt.html"
    form_class = UserPromptForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)

        answer_id = self.request.GET.get("answer", None)
        if answer_id:
            try:
                user_prompt = UserPrompt.objects.get(id=answer_id)
                context["answer"] = user_prompt.response
            except UserPrompt.DoesNotExist:
                return reverse('magicai:user_prompt')
        return context


    def form_valid(self, form):
        user_prompt =  form.cleaned_data["prompt"]
        user_prompt_obj = form.save(commit=False)
        user_prompt_obj.user = self.request.user

        # ai Code Logic + Save to Response Table
        response_data_obj = OpenAiClient.send_prompt(user_prompt)

        user_prompt_obj.response = response_data_obj
        user_prompt_obj.save()
        return super().form_valid(form)


    def get_success_url(self):
        prompt = self.request.user.get_latest_prompt()
        return f"{reverse('magicai:user_prompt')}?answer={prompt.id}"
