with open('sentences.txt','r') as sentencesFile:
    S = sentencesFile.read().split('\n')

with open('terms.txt','r') as termsFile:
    T = termsFile.read().split('\n')


'''Assumption - The term can be used only once. Say if a term matches in one sentence, we can not use it in another.

Algo
We will generate weights for each sentence against the list of terms.
So we will have a HashMap where will store a term as key and its corresponding weight as the value against the sentence.
The sentences having max weights will be considered first and in the process the terms considered in the first, will be removed from the others.
'''







'''Weights -> Loop over the sentences to generate weight map against each term.'''

def mapSentencesAndTermsToWeights(sentences, terms):
    weights = []
    i = 0
    for sentence in sentences:
        termWeights = []
        for term in terms:
            if term in sentence:
                termWeights.append(term)
        weights.append({'sentenceIndex': i,'sumOfWeights' : len(termWeights),'terms': termWeights})
        i += 1
    return filterAndSortWeights(weights)





'''Helper recursive function to process the result from weights'''
def processStringsFromWeights(weights, result, sentences, termsUsed):
    if len(weights) == 0:
        return result 
    result.append(sentences[weights[0]['sentenceIndex']])
    termsUsed = termsUsed + weights[0]['terms']

    i = 0

    copy = weights.copy()
    while(i < len(copy)):

        for term in termsUsed:

            if term in copy[i]['terms']:
                currIndex = weights.index(copy[i])

                del weights[currIndex]
                break
            else:
                continue
        i = i + 1
        


    
    '''Call the function again to process the remaining weights'''
    return processStringsFromWeights(weights, result, sentences, termsUsed)

'''Helper function to filter and sort the weights'''
def filterAndSortWeights(weights):
    weights = [ weight for weight in weights if weight['sumOfWeights'] > 0]
    from operator import itemgetter
    weights = sorted(weights, key=itemgetter('sumOfWeights'), reverse = True)
    return weights


W = mapSentencesAndTermsToWeights(S, T)
R = processStringsFromWeights(W, [], S, [])

print(R)