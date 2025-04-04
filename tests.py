import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_create_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    assert len(question.choices) == 3
    assert question.choices[0].text == 'a'
    assert not question.choices[0].is_correct
    assert question.choices[1].text == 'b'
    assert question.choices[1].is_correct
    assert question.choices[2].text == 'c'
    assert not question.choices[2].is_correct

def test_remove_choice_by_id():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    assert len(question.choices) == 3
    
    question.remove_choice_by_id(2)

    assert len(question.choices) == 2
    assert question.choices[0].text == 'a'
    assert not question.choices[0].is_correct
    assert question.choices[1].text == 'c'
    assert not question.choices[1].is_correct

def test_remove_all_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', False)

    assert len(question.choices) == 3
    
    question.remove_all_choices()

    assert len(question.choices) == 0

def test_select_choices_with_larger_list_ids():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    with pytest.raises(Exception):
        question.select_choices([1,2])

def test_select_choices_with_correct_question_id():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    selectedQuestions = question.select_choices([2])
    assert len(selectedQuestions) == 1
    assert selectedQuestions[0] == 2

def test_select_choices_with_incorrect_question_id():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    selectedQuestions = question.select_choices([1])
    assert len(selectedQuestions) == 0

def test_select_choices_with_multiple_correct_question_ids():
    question = Question(title='q1', max_selections = 3)
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', True)
    question.add_choice('d', False)
    question.add_choice('e', True)
    question.add_choice('f', False)
    selectedQuestions = question.select_choices([2, 3, 5])
    assert len(selectedQuestions) == 3
    assert selectedQuestions[0] == 2
    assert selectedQuestions[1] == 3
    assert selectedQuestions[2] == 5

def test_select_choices_with_correct_and_incorrect_questions_ids():
    question = Question(title='q1', max_selections = 3)
    
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', True)
    question.add_choice('d', False)
    question.add_choice('e', True)
    question.add_choice('f', False)
    selectedQuestions = question.select_choices([2, 4, 6])
    assert len(selectedQuestions) == 1
    assert selectedQuestions[0] == 2

def test_set_correct_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', False)

    question.set_correct_choices([2,3])
    assert question.choices[1].is_correct
    assert question.choices[2].is_correct

def test_set_correct_choices_with_invalid_id():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    with pytest.raises(Exception):
        question.set_correct_choices([3])

@pytest.fixture
def create_question_with_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)

def test_add_question_with_invalid_text(create_question_with_multiple_choices):
    with pytest.raises(Exception):
        question.add_choice('')
    with pytest.raises(Exception):
        question.add_choice('a' * 100)

def test_remove_choice_by_id_with_invalid_id(create_question_with_multiple_choices):
    with pytest.raises(Exception):
        question.remove_choice_by_id(4)