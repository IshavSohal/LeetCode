import itertools
import collections


def checkInclusion1(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    perms = itertools.permutations(s1, len(s1))
    perms_list = []

    for permutation in perms:
        s = ""
        for letter in permutation:
            s += letter
        perms_list.append(s)

    for perm in perms_list:
        if perm in s2:
            return True

    return False


def checkInclusion2(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    # For each substring in s2 of lenth len(s1), check if its a permutation
    # of s1
    i = 0
    j = len(s1) - 1

    while j < len(s2):
        d = collections.defaultdict(int)
        s2_substring = s2[i:j+1]

        for letter in s2_substring:
            d[letter] += 1

        for letter in s1:
            d[letter] -= 1

        if not any(d.values()):
            return True

        i += 1
        j += 1

    return False


def checkInclusion3(s1,s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if s1 in s2 or s1[::-1] in s2:
        return True
    chain_count = 0
    s1_cpy = (s1 + '.')[:-1]

    for i in range(len(s2)):

        # Start of a chain
        if s2[i] in s1_cpy:
            chain_count += 1
            s1_cpy = s1_cpy.replace(s2[i], "", 1)

        else:
            chain_count = 0
            s1_cpy = (s1 + '.')[:-1]

        if chain_count == len(s1):
            return True

    return False


if __name__ == "__main__":
    print(checkInclusion2("hello", "ooollheoefne"))
    s1 = "tivgqswqmviletlomdojhngauvxduwgeqzjtihgdzxgczqphjjnrzntyivtpcpijrvyfeshbqbxzbuocdthreyikarjayktsgfvzpglbbuxxrxeumgxemspnagxtskvzvsvnkngsoaakiucksugcernxuqcbyzljvgnogxmodasqcvtmbiwiekntfalzrwnatpsdlqrwropxahmnigzpyrjlmucdbjgbgkoryiptjnuxmlukeqrenvncidktgafvxglmpteecytyfzngzgwmmmjtafgblawqsynhuzlvpgrvmnufsyqbottfdahnkmjlgjazfvvfktvowocrotcgdndvfujvejvvuhpoisaugjuugnvqhzmmxgpaiapxaexlfvymcuwjmnergdcpxhzwamtcakkluwoetwnsynblwmuuetsmmqurykkulyoccoswggplnumrgjwojxanznhfhjymunwllihvpmmorxheaskwljthdnkmpywlnxpgrzzcjrrkevcyskdkapgvvdagizykznzqdxoapxmngsmooqbvimrfttmjcns"
    s2 = "oxjpbkbjgvkxejowukuhulglusrjaeotimsfnfkysgtqjjfpvmhjkemfrnygwkquznthgznigouhznlylexmdgfrrznhjnbatrtxbgbiypsrtbndhzkofniivtwjdxamwienxxbetvfzcbmutrksjltsmpavjobipmmalibntgasxmuzejinnuxecduzvepdbikjjizktgebbmojfikzpmqyocoibwtqfhwutxzowzuvcizvmryukztvpzbdtussrpkofulfbiawyofcksrbhhnrytauddjdssipypnqepftzfkvdemhnpindikkfkijlvlkhdgdmmilbswpefawneibrbclkmuzodwatelmyhuzzreqibhbzrhpfuhyijhzziywjukuzuceqpubfpldzydqmmmrdhbyygegrdytbtrfvwaihsdaavckseosrkoplrpsnlqpuuhgtjesxdzcodptkinjuaidnavrhzdhlymmzmsosqlcyaqgkwtitrenllekrywjzkbrfqasyyaifwdxiacwjixiksnoozkpjsakierftnjimbklegdluisbacwdoqrhrpollmqilinamlltytudelonnozkgfwlhumjcbwenatervgtpalompefhcyrfedxfujmmmzzfshforbvijwydfrojjxefqatpviosbvofkmhnrhefpsqoaxcjxakjtgffphssgjxooxfzlihxtxussvhbvmihenvzojmsscarelmtyavwolzgsaanyqhzaklvqcyxzuptquvhvrjotopftmkqiynjioytaeonymisnilfbrtabifivcmtlauyqghtksersfrjhgolsjvzamiicpsjmiomzcoooluhwqxgwigvkcijrxiwperfiarrxeoefwyypwymzapwlvcybkteqdmydueonshnqtziodhwatepmywkvrwjniogqstqmviletlomdojhngauvxdupgnqzjtihgdzxgczqphjjnrzntyivtpcpijrmyfeshmqbxzbuocdthweyikarjayatsgfvkpglebuhsrxeumgxemxpnagxtskvzvsvnrngsoaakiucksugcernxuqcbuzljvgnomxmouasqvvtmbiribknwfalzrwtatpsdlqrjropxahmnigzpyrjlmucfbjgbgkorciptjnuxglukeqreevogydktgkdvxglmpteecytyfzngzgwmmtjtadgblawqsyvhuzlvpgkvmnufsnqbonnfdhhnkmrlgjazfnvfwtvowncrvtccdndvfujxejvvyhpoisaugjuugtvqhzvzvgpaiapxeexlznymcuwwmnergdcpxhzwamtcakkluwoetwnsinblwmuuebsmmqurykkylyoccoswggplndmrgjkojxayztxfhjymunwllihvpmmojxhqaskwljtadnkmpywlnxpgrzzcjrrkavcyskdzawgvvdmgimykfnzqfxoapxangsmooebvimrfttmjcusqrsnsylfkroqehtxtwwoipyjvpdxaqiuvmcrchhmzosnpddgxjxiftxvhgzefosjptdtkdwxjxugcmgnhlnkcifzphodnqrmbgoakbmlaxifmburvxnspqbpoansvhofxvbnzrmodizuawhtmvcbaeqzrxyvhhxtaqdqinaoykrjhebyljqewdxfurqfsoavdekujqzbkeqgyqzgeikljybmbajjefrnobiendssudpdmfuoffpdetsaepcivxmllufdgutwypcwcbiilgzrlzqqyyntgmtylqgpvlzfdqwviiqrfpxodmfodqgmpxbtkqvypwoqymnhuywkyzwdpaxewimesymojapavboblcomhbdywfthgtqhxabmubxcuzrrxjrfpzdbdjrynrgdpederxsapxbbikenkdmriqifsqqzqyzrcvbgqrmppygzigojccstwunljsdssfwescplglunrvrlimuafofwcyhlpbtoqyuzvxwrpattzpnwuhymbgplnknqznwjrdwclxuaeldbyrisjddshqnyporwnvjypsjypsdgjifbszalilfvvrrokqdiygluxprovcirbtzbtkwojihuwrhjrhtkepncitjsafgzdatkgsfhmkujbagnpgarhqpsrosymvpaewqgjgydqtxxjxzyneirrobwanhqnkmuusssnroznteeodtzkcsiprqueeaeecxvbhizgzbnyudxlrkafobyexvnfcqbdnixhtgfewiwikhngtsuphiglpfqdhcphoysjhnbuacdakybdceirnrgljuppcheczoblstclaswjcrjjwcfhspncuzbhptenkfosdmrfvzfleaczzlpsepmdosluuoczhxzakeovxvkdyvkwbqmknvnocdgywhxqeztdvwinqiydzaxytxgqzxdqibihagybivulxuzppgulxodfdntqgjezmqymebpcdyivduuooosfcsvhwtvziavqtwtwgyxiirffetjikomjaxxbzwxgtvoxzryndgbbldilphthxhugbjrzxygijlvfppiuffopgqkedrlesllclcislnwmfnfrodettzannvdrzfmigtaqryjjnhrywjpugkkmozgyuxkadrygttbdfgtgzripbawbizshhaunnlsqxvnuwgjwxifgxvcebtawuejmfwstiqwzzfhvvviforzaoszdquryfqnieipdjxovsokiiozewvmrgoequsvmspdzrhadafaiyrfrnlnjtytudfkfeqzgnovbtcpnlazpgccofexuztfprbszugoqcrtyswqlrndaoyodbauyusmybtfnvsulgbtgadevgkjmstlmvbzayxomrlzxdmrmzwelndrvoxlvqfoaehpdqvdmquiimnxjbsimwjelpiymgehqyplhxheeswovzmoduvravlnaydcjtwmekgzqcvarmxxvhxemswbwgwzaxamwsnuzmicvlzirbokwayebvkbbgdvkszvaitppnrpfargetgcltsvfjpanogzumbqmxicqucrljyiaozswgliceulwoepajkttzqxvhkmfuinzgaucxggdcaxmwbxykghtcmsohnqvfeewjtekgtbonhnwozwykfinbqkhbhxxmkkdrltxcisynanfxfmykwvtsfdihvmruxvzwtkghleqwsmlqmmqovubwtstdygqcyybhzaagwblobbuxcjdxviwcozsvejpesmyxahimpoxpqlksfhnfzurwanfgbmczxtqmawezfqpwytodsbftdogegwktafkpvjnqzzduhuybzncynivlcopzuuwugpksstgzqyolfohfjhwsghmogmqawxmxhewrvjvfxldxcfwwcyvcsyeujcivgemi"
    print(checkInclusion2(s1, s2))
