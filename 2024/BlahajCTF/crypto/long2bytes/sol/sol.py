# solve
# https://eprint.iacr.org/2016/215.pdf, Simultaneous Diophantine approximation approach (SDA)
# Observations during chall creation:
# * z is needed even when i try to pad out the number to be large enough :V
# (i.e. using x = <much larger f0> + randint(1,2**64) doesnt work for some reason)

from sage.all import Matrix, ZZ, RealField
from hashlib import md5

H = lambda x:md5(str(x).encode()).hexdigest()
R = RealField(8192)
out = R("162.23252214274515943397782287355540190005746146684565906972122466888759773035502086481095042428501607951460848654954469141687515308929897489683350595379571914921913582470444773305710706452084964142829574022629622094317603084027778853986273962642535581215322932391708352930540505934778578940251468586431597827418921183554011990308468098651364548086321976843740439065487356258045815818006311576925691384898136116756892330431130459043518026980550152831715646932014262967833645972306383217267098657418889650872862797841449211480031496381522546518273629692498153540617567002964496877648185214579912119809337941113857800410204072297252140103528866418763903348525491462117367299205513670821307620979590835429881355194032997063501777833935950398498719702741323772880906606529182711257534418325387700544735555238457100977042343774629386706321788240871835734018852670904316501005519081287430031815644820486229221422423039045516213391398927923975964410483042929052050875325897872818029299754005952899412240112668544916296699877229780273373424763968537781231168549678901498535474525682344654273950240396850590930944628870798216614639675182297442360112270664812966014045259425377210413361611614195860358415252592912092224163343756244181892101497675299086220717572772226689268608620581454111544871923353685948261796406858102884358746569137449345736207423645787805050711703348686172635798007886140745894359778838446815914083623492655426035215587249528092249799542512728786415699262271326460806092265670856509974154088707208225259811452766700034539287854658549997739631909073349212417534910551278049388563742957463248418216221406042614201232730971618053966763210340559786549694731507432561389312698358428273988542641918786610475974478344837321725030943267769312960122841043084479216780873868560480674531945607189170077796806076268690930152767502419413125963418373154505774976468873515501750506683862375445757578198244802619257375338833713116227822233309342467903592970388761318767438808114940864882107393248437992637562997790267993343374583514343618770863918755033259993602631619063000526991026147930201483630043182270091622997598993506278739089157555245018550782747759618821844384758920358023052375330761546541785689374093215979344381588469444475182745208421380747286000851932410735830476820242558615192006833052003014710751288480795314652839115325006883067212472079002697231724560481530509506356438724770753147690713889622153248044847111239767394015194396749376202543123150240340")
hf0 = '116dde5968e806d826fa86c06aedab25'
hf1 = '34d32c71edc577fe3ba3414e1d6f9be2'

# Get x,y from out where x/y is very, very close to out
x, y = out.nearby_rational(max_denominator=2**3072).as_integer_ratio()

# x/y approx equal to f0/f1
# thus x*f1 - y*f0 is relatively small. We exploit this with LLL to recover f0 and f1

flag = b''
M = Matrix(ZZ, [[2**64,y],[0, -x]]) # 2**64 is done to scale the 0-th column such that 2**64 * f0 is of similar bit length to y*f0 - x*f1
ff0 = abs(M.LLL()[0,0]) // 2**64
while H(ff0) != hf0:
    ff0 -= 1
flag += ff0.to_bytes(129, "big").lstrip(b'\x00')

M = Matrix(ZZ, [[2**64,x],[0, -y]]) # repeat to recover ff1
ff1 = abs(M.LLL()[0,0]) // 2**64
while H(ff1) != hf1:
    ff1 -= 1
flag += ff1.to_bytes(129, "big").lstrip(b'\x00')

print(flag)