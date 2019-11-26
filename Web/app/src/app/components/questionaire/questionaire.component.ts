import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import { UserService } from '../../service/user.service'

@Component({
  selector: 'app-questionaire',
  templateUrl: './questionaire.component.html',
  styleUrls: ['./questionaire.component.css']
})
export class QuestionaireComponent implements OnInit {

  questionStack;
  currentIndex = 0;
  constructor(private userService:UserService) {  }

  ngOnInit() {
    this.fetchQuestions();
    // this.questionStack = [
    //   {
    //       "question_id": "q1",
    //       "question_text": "I would",
    //       "answer_1_id": "1a",
    //       "answer_1": "/resources/question_images/1a.jpg",
    //       "answer_2_id": "1b",
    //       "answer_2": "/resources/question_images/1b.jpg"
    //   },
    //   {
    //       "question_id": "q3",
    //       "question_text": "My place is",
    //       "answer_1_id": "3a",
    //       "answer_1": "/resources/question_images/3a.jpg",
    //       "answer_2_id": "3b",
    //       "answer_2": "/resources/question_images/3b.jpg"
    //   },
    //   {
    //       "question_id": "q4",
    //       "question_text": "When I get stressed",
    //       "answer_1_id": "4a",
    //       "answer_1": "/resources/question_images/4a.jpg",
    //       "answer_2_id": "4b",
    //       "answer_2": "/resources/question_images/4b.jpg"
    //   },
    //   {
    //       "question_id": "q6",
    //       "question_text": "If things don't go my way",
    //       "answer_1_id": "6a",
    //       "answer_1": "/resources/question_images/6a.jpg",
    //       "answer_2_id": "6b",
    //       "answer_2": "/resources/question_images/6b.jpg"
    //   },
    //   {
    //       "question_id": "q7",
    //       "question_text": "How I treat people in general",
    //       "answer_1_id": "7a",
    //       "answer_1": "/resources/question_images/7a.jpg",
    //       "answer_2_id": "7b",
    //       "answer_2": "/resources/question_images/7b.jpg"
    //   },
    //   {
    //       "question_id": "q8",
    //       "question_text": "Mornings be like",
    //       "answer_1_id": "8a",
    //       "answer_1": "/resources/question_images/8a.jpg",
    //       "answer_2_id": "8b",
    //       "answer_2": "/resources/question_images/8b.jpg"
    //   },
    //   {
    //       "question_id": "q9",
    //       "question_text": "After failing, next day I'm like",
    //       "answer_1_id": "9a",
    //       "answer_1": "/resources/question_images/9a.jpg",
    //       "answer_2_id": "9b",
    //       "answer_2": "/resources/question_images/9b.jpg"
    //   },
    //   {
    //       "question_id": "q10",
    //       "question_text": "New cuisine?",
    //       "answer_1_id": "10a",
    //       "answer_1": "/resources/question_images/10a.jpg",
    //       "answer_2_id": "10b",
    //       "answer_2": "/resources/question_images/10b.jpg"
    //   },
    //   {
    //       "question_id": "q11",
    //       "question_text": "On birthday, I'm",
    //       "answer_1_id": "11a",
    //       "answer_1": "/resources/question_images/11a.jpg",
    //       "answer_2_id": "11b",
    //       "answer_2": "/resources/question_images/11b.jpg"
    //   },
    //   {
    //       "question_id": "q13",
    //       "question_text": "People rely on me like",
    //       "answer_1_id": "13a",
    //       "answer_1": "/resources/question_images/13a.jpg",
    //       "answer_2_id": "13b",
    //       "answer_2": "/resources/question_images/13b.jpg"
    //   },
    //   {
    //       "question_id": "q15",
    //       "question_text": "On hearing a new idea, my brain",
    //       "answer_1_id": "15a",
    //       "answer_1": "/resources/question_images/15a.jpg",
    //       "answer_2_id": "15b",
    //       "answer_2": "/resources/question_images/15b.jpg"
    //   },
    //   {
    //       "question_id": "q16",
    //       "question_text": "How I reply to loud people",
    //       "answer_1_id": "16a",
    //       "answer_1": "/resources/question_images/16a.jpg",
    //       "answer_2_id": "16b",
    //       "answer_2": "/resources/question_images/16b.jpg"
    //   },
    //   {
    //       "question_id": "q18",
    //       "question_text": "When I Netflix",
    //       "answer_1_id": "18a",
    //       "answer_1": "/resources/question_images/18a.jpg",
    //       "answer_2_id": "18b",
    //       "answer_2": "/resources/question_images/18b.jpg"
    //   },
    //   {
    //       "question_id": "q21",
    //       "question_text": "Kind of leader I am",
    //       "answer_1_id": "21a",
    //       "answer_1": "/resources/question_images/21a.jpg",
    //       "answer_2_id": "21b",
    //       "answer_2": "/resources/question_images/21b.jpg"
    //   },
    //   {
    //       "question_id": "q25",
    //       "question_text": "Cop: You're driving fast! Me:",
    //       "answer_1_id": "25a",
    //       "answer_1": "/resources/question_images/25a.jpg",
    //       "answer_2_id": "25b",
    //       "answer_2": "/resources/question_images/25b.jpg"
    //   },
    //   {
    //       "question_id": "q42",
    //       "question_text": "If someone gets me a chocolate",
    //       "answer_1_id": "42a",
    //       "answer_1": "/resources/question_images/42a.jpg",
    //       "answer_2_id": "42b",
    //       "answer_2": "/resources/question_images/42b.jpg"
    //   },
    //   {
    //       "question_id": "q44",
    //       "question_text": "My emotions during the day",
    //       "answer_1_id": "44a",
    //       "answer_1": "/resources/question_images/44a.jpg",
    //       "answer_2_id": "44b",
    //       "answer_2": "/resources/question_images/44b.jpg"
    //   },
    //   {
    //       "question_id": "q45",
    //       "question_text": "If I were to imagine a story",
    //       "answer_1_id": "45a",
    //       "answer_1": "/resources/question_images/45a.jpg",
    //       "answer_2_id": "45b",
    //       "answer_2": "/resources/question_images/45b.jpg"
    //   },
    //   {
    //       "question_id": "q46",
    //       "question_text": "If it comes to holding a conversation",
    //       "answer_1_id": "46a",
    //       "answer_1": "/resources/question_images/46a.jpg",
    //       "answer_2_id": "46b",
    //       "answer_2": "/resources/question_images/46b.jpg"
    //   },
    //   {
    //       "question_id": "q48",
    //       "question_text": "When I have to clean",
    //       "answer_1_id": "48a",
    //       "answer_1": "/resources/question_images/48a.jpg",
    //       "answer_2_id": "48b",
    //       "answer_2": "/resources/question_images/48b.jpg"
    //   },
    //   {
    //       "question_id": "q52",
    //       "question_text": "My general behaviour",
    //       "answer_1_id": "52a",
    //       "answer_1": "/resources/question_images/52a.jpg",
    //       "answer_2_id": "52b",
    //       "answer_2": "/resources/question_images/52b.jpg"
    //   }
    // ];
  }

  executeAndfetchNextQuestion(answerId, questionId){
    console.log('-----', answerId, questionId);
    let userResp = {
      'public_id' : localStorage.getItem('token'),
      'question_id' : questionId,
      'answer_id' : answerId
    };
    this.userService.submitUserResponse(userResp).subscribe((response)=>{
      console.log(response);
     });
    this.currentIndex++;
  }

  fetchQuestions(){
    this.userService.getUserQuestions().subscribe((response)=>{
      this.questionStack = response;
     });
  }

}
