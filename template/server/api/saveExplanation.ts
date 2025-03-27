import fs from 'fs';
import path from 'path';

export default defineEventHandler(async (event) => {
    const { questionId, explanation }: { questionId: string; explanation: string} = await readBody(event);
    const filePath = path.resolve('data/ia', `${questionId}_ia_explanation.txt`);

    console.log(filePath)
    try {
        // Escrever os dados no arquivo
        fs.writeFileSync(filePath, explanation, { encoding: 'utf8' });
        return { status: 'success', message: 'Explanation saved successfully' };
    } catch (error) {
        return { status: 'error', message: 'Failed to save explanation', error };
    }
});