from django import forms
from .models import Board, Comment, CommentReply, Category

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

def category_choice():
    choices = (
    ('1', '취업'),
    ('2', '직장'),
    ('3', '공부'),
    ('4', '학교'),
    ('5', '시험'),
    ('6', '알바'),
    ('7', '일상'),
    ('8', '관계'),
    ('9', '웃긴'),
    ('10', '여행'),
    ('11', '취미'),
    ('12', '기타'),
)

    return choices


class PostForm(forms.ModelForm):
    b_name =  forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 2,
        'cols': 10,
        'placeholder': '작품명', }))
    
    b_intro1 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': '당신의 slip을 들려주세요.', }))
    
    b_intro2 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': 'Slip한 이유가 무엇일까요?', }))
    
    b_intro3 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': '다음엔 어떻게 하면 좋을까요?', }))
    
    suc_intro1 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': '당신의 성공을 들려주세요.', }))
    
    suc_intro2 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': '성공한 이유가 무엇일까요?', }))
    
    suc_intro3 = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 9,
        'cols': 20,
        'placeholder': '나에게 하고 싶은 말', }))
    
    # k_no = forms.ChoiceField(label='', widget=forms.Select(), choices =category_select)
    

    class Meta:
        model = Board
        fields = ['b_name', 'b_intro1', 'b_intro2', 'b_intro3', 'suc_intro1', 'suc_intro2', 'suc_intro3', 'b_img']
        
        # widgets = {
        #     'k_no' : forms.Select(choices=category_select)
        # }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['k_no'].choices = category_choice()
        
        
        
class CommentForm(forms.ModelForm):
    c_content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': 'Slip 작품에 대한 감상평을 적어 주세요.', }))

    class Meta:
        model = Comment
        fields = ['c_content']
        
class CommentReplyForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '대댓글을 입력해주세요.', }))

    class Meta:
        model = CommentReply
        fields = ['content']
