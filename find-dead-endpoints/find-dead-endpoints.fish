set apiPath $argv[1]
set fePath $argv[2]

set operationIds (rg -I "operationId:" $apiPath | sd "^.*operationId: " "")

for operationId in $operationIds
  echo $operationId:
  rg -c api.$operationId $fePath
end
