# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scmddzcf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scmddzcf.proto',
  package='Dzcf',
  syntax='proto3',
  serialized_pb=_b('\n\x0escmddzcf.proto\x12\x04\x44zcf\"\x19\n\tImagePath\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x1d\n\x08Jsondata\x12\x11\n\tdata_json\x18\x01 \x01(\t25\n\x04\x44\x61ta\x12-\n\x08TextDzcf\x12\x0f.Dzcf.ImagePath\x1a\x0e.Dzcf.Jsondata\"\x00\x42&\n\x11io.grpc.scmd.DzcfB\tDzcfProtoP\x01\xa2\x02\x03TCRb\x06proto3')
)




_IMAGEPATH = _descriptor.Descriptor(
  name='ImagePath',
  full_name='Dzcf.ImagePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='Dzcf.ImagePath.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=49,
)


_JSONDATA = _descriptor.Descriptor(
  name='Jsondata',
  full_name='Dzcf.Jsondata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_json', full_name='Dzcf.Jsondata.data_json', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['ImagePath'] = _IMAGEPATH
DESCRIPTOR.message_types_by_name['Jsondata'] = _JSONDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImagePath = _reflection.GeneratedProtocolMessageType('ImagePath', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEPATH,
  __module__ = 'scmddzcf_pb2'
  # @@protoc_insertion_point(class_scope:Dzcf.ImagePath)
  ))
_sym_db.RegisterMessage(ImagePath)

Jsondata = _reflection.GeneratedProtocolMessageType('Jsondata', (_message.Message,), dict(
  DESCRIPTOR = _JSONDATA,
  __module__ = 'scmddzcf_pb2'
  # @@protoc_insertion_point(class_scope:Dzcf.Jsondata)
  ))
_sym_db.RegisterMessage(Jsondata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021io.grpc.scmd.DzcfB\tDzcfProtoP\001\242\002\003TCR'))

_DATA = _descriptor.ServiceDescriptor(
  name='Data',
  full_name='Dzcf.Data',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=82,
  serialized_end=135,
  methods=[
  _descriptor.MethodDescriptor(
    name='TextDzcf',
    full_name='Dzcf.Data.TextDzcf',
    index=0,
    containing_service=None,
    input_type=_IMAGEPATH,
    output_type=_JSONDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATA)

DESCRIPTOR.services_by_name['Data'] = _DATA

# @@protoc_insertion_point(module_scope)