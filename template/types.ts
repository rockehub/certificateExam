// types.ts

export interface Option {
    text: string;
}

export interface Question {
    Question: string;
    QuestionText: string;
    Code?: boolean,
    Lang?: string,
    Content?: string,
    Options: Option[];
    CorrectAnswer: string;
}

export interface Exam {
    id: string;
    name: string;
    min_required: number;
    max_questions: number;
    questions: Question[];
}
