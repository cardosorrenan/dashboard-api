class Address < ActiveRecord::Base
  belongs_to :addressable, polymorphic: true

  has_enumeration_for :state, create_helpers: true
end
