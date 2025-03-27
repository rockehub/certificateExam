import fs from 'fs';
import path from 'path';

export default defineEventHandler(async (event) => {
    const { examId }: { examId: string } = await getQuery(event);

    const filePath = path.resolve('data/exams', `${examId}.json`);

    try {

        if (fs.existsSync(filePath)) {
            const exam = JSON.parse(fs.readFileSync(filePath, 'utf8'));
            return { ...exam };
        } else {
            return { explanation: null };  // Retorna null se o arquivo não existir
        }
    } catch (error) {
        return { status: 'error', message: 'Failed to retrieve explanation', error };
    }
});