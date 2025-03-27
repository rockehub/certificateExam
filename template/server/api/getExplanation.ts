import fs from 'fs';
import path from 'path';

export default defineEventHandler(async (event) => {
    const { questionId }: { questionId: string, examId: string } = await getQuery(event);

    const filePath = path.resolve('data/ia', `${questionId}_ia_explanation.txt`);

    try {
        // Verificar se o arquivo existe
        if (fs.existsSync(filePath)) {
            const explanation = fs.readFileSync(filePath, 'utf8');
            return { explanation };
        } else {
            return { explanation: null };  // Retorna null se o arquivo não existir
        }
    } catch (error) {
        return { status: 'error', message: 'Failed to retrieve explanation', error };
    }
});