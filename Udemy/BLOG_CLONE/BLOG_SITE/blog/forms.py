from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')  # the user can edit these fields

        widgets = {
            # the title field is now connected to the textinputclass in css files
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            # the text field is now connected to the class vvvvvv
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')  # the user can edit these fields

        widgets = {
            # the author field is now connected to the textinputclass in css files to make it appear similar to the
            # title  field in the Post class
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
