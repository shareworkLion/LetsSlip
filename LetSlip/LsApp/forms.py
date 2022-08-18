from django import forms
from .models import Post, Comment, CommentReply

category_select = (
    ('취업', '취업'),
    ('직장', '직장'),
    ('공부', '공부'),
    ('학교', '학교'),
    ('시험', '시험'),
    ('알바', '알바'),
    ('일상', '일상'),
    ('관계', '관계'),
    ('웃긴', '웃긴'),
    ('여행', '여행'),
    ('취미', '취미'),
    ('기타', '기타'),
)


class PostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.', }))

    class Meta:
        model = Post
        fields = ['title', 'body', 'photo', 'category']
        
        widgets = {
            'category' : forms.Select(choices=category_select)
        }
        
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': 'Slip 작품에 대한 감상평을 적어 주세요.', }))

    class Meta:
        model = Comment
        fields = ['comment']
        
class CommentReplyForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '대댓글을 입력해주세요.', }))

    class Meta:
        model = CommentReply
        fields = ['content']