from django import forms
from .models import Feedback, NewsArticle, NewsSource


class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['rating', 'comment', 'user_name', 'user_email', 'is_helpful']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '5',
                'required': True
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your thoughts about this article...'
            }),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name (optional)'
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email (optional)'
            }),
            'is_helpful': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'rating': 'Rating (1-5)',
            'comment': 'Comment',
            'user_name': 'Name',
            'user_email': 'Email',
            'is_helpful': 'Was this article helpful?',
        }


class NewsFilterForm(forms.Form):
    region = forms.CharField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Filter by Region'
    )
    category = forms.ChoiceField(
        required=False,
        choices=[('', 'All Categories')] + NewsArticle._meta.get_field('category').choices,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Filter by Category'
    )
    source = forms.ModelChoiceField(
        required=False,
        queryset=None,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Filter by Source'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].queryset = NewsSource.objects.filter(is_active=True)

