// types.ts

export interface Option {
    text: string;
}

export interface Question {
    Question: string
    QuestionText: string
    Options: Alternative[]
    CorrectAnswer: string
    Code?: boolean
    Lang?: string
    Content?: string
}

export interface Alternative {
    number: number
    question: string
}

export interface Exam {
    name: string
    id: string
    min_required: number
    max_questions: number
    questions: Question[]
}



export interface PromptFinal {
    candidates: Candidate[]
    usageMetadata: UsageMetadata
    modelVersion: string
}

export interface Candidate {
    content: Content
    finishReason: string
    avgLogprobs: number
}

export interface Content {
    parts: Part[]
    role: string
}

export interface Part {
    text: string
}

export interface UsageMetadata {
    promptTokenCount: number
    candidatesTokenCount: number
    totalTokenCount: number
    promptTokensDetails: PromptTokensDetail[]
    candidatesTokensDetails: CandidatesTokensDetail[]
}

export interface PromptTokensDetail {
    modality: string
    tokenCount: number
}

export interface CandidatesTokensDetail {
    modality: string
    tokenCount: number
}