import fs from 'fs';
import path from 'path';

export default defineEventHandler(async () => {
    const examsDir = path.resolve('data/exams');

    try {
        if (!fs.existsSync(examsDir)) {
            return { status: 'error', message: 'Exams directory not found' };
        }

        const files = fs.readdirSync(examsDir);
        const exams = files
            .filter(file => file.endsWith('.json'))
            .map(file => {
                const filePath = path.join(examsDir, file);
                const examData = JSON.parse(fs.readFileSync(filePath, 'utf8'));

                return {
                    name: examData.name || "Unknown",
                    id: examData.id || path.basename(file, '.json'),
                    min_required: examData.min_required || 0,
                    max_questions: examData.max_questions || 0
                };
            });

        return { ...exams };
    } catch (error) {
        return { status: 'error', message: 'Failed to retrieve exams', error };
    }
});
